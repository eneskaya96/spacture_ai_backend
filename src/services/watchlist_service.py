import logging
from typing import Optional, List, Dict

from src.api.models.dto.watchlist.watchlist_face_detection_request_dto import WatchlistFaceDetectionRequestDto
from src.api.models.dto.watchlist.watchlist_face_detection_response_dto import WatchlistFaceDetectionResponseDto
from src.api.models.dto.watchlist.watchlist_request_dto import WatchlistRequestDto
from src.domain.watchlist.entities.watchlist import Watchlist
from src.domain.watchlist.entities.watchlistFaceDetection import WatchlistFaceDetection
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
from src.services.base.base_service import BaseService
from src.services.detected_images import DetectedFaceService


class WatchlistService(BaseService):
    logger = logging.getLogger(__name__)

    def __init__(self, socketio, uow: Optional[UnitOfWork] = None) -> None:
        self.socketio = socketio
        self.detected_face_service = DetectedFaceService(socketio)
        super().__init__(uow)

    def create_watchlist(self, watchlist_request_dto: WatchlistRequestDto) -> Watchlist:
        """
        Create a new watchlist, notify the microservice and returns it
        :param watchlist_request_dto
        """

        face_detection = self.uow.face_detection.get(watchlist_request_dto.face_detection_id)

        if not face_detection:
            self.logger.error(f'Face detection id: {watchlist_request_dto.face_detection_id} is not found on DB')

        new_watchlist = Watchlist.create_watchlist(watchlist_request_dto.company_id,
                                                   watchlist_request_dto.face_detection_id)

        with self.uow:
            self.uow.watchlist.insert(new_watchlist)

        self.logger.info(f'Watchlist detection is created for  request: {watchlist_request_dto}')

        return new_watchlist

    def notify_watchlist_detected(self, watchlist_face_detection_id):
        """
        Notifies the newly detected watchlist
        :param watchlist_face_detection_id
        """

        # TODO make join sql
        watchlist_face_detection = self.uow.watchlist_face_detection.get(watchlist_face_detection_id)

        watchlist = self.uow.watchlist.get(watchlist_face_detection.watchlist_id)

        old_face_detection = self.uow.face_detection.get(watchlist.face_detection_id)
        new_face_detection = self.uow.face_detection.get(watchlist_face_detection.face_detection_id)

        detected_person = {
            "id": old_face_detection.id,
            "image_url": old_face_detection.image_url,
            "match_image_url": new_face_detection.image_url,
            "created_date": watchlist_face_detection.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "thread": True
        }

        self.socketio.emit('new_detection', {'data': [detected_person]}, namespace='/')

    def create_watchlist_face_detection(self, watchlist_face_detection_request_dto: WatchlistFaceDetectionRequestDto):
        """
        Create a new watchlist face detection and returns it
        :param watchlist_face_detection_request_dto
        """
        watchlist = self.uow.watchlist.get_watchlist_by_face_detection_id(
            watchlist_face_detection_request_dto.old_face_detection_id)
        if not watchlist:
            self.logger.error(
                f'Watchlist item with old_face_detection id: {watchlist_face_detection_request_dto.old_face_detection_id} '
                f'is not found on DB')

        if not self.uow.face_detection.get(watchlist_face_detection_request_dto.face_detection_id):
            self.logger.error(
                f'Face detection with id: {watchlist_face_detection_request_dto.face_detection_id} is not found on DB')

        new_watchlist_face_detection = WatchlistFaceDetection.create_watchlist_face_detection(
            watchlist.id,
            watchlist_face_detection_request_dto.face_detection_id)

        with self.uow:
            self.uow.watchlist_face_detection.insert(new_watchlist_face_detection)

        self.logger.info(f'Watchlist face detection is created for  request: {watchlist_face_detection_request_dto}')

        old_face_detection = self.uow.face_detection.get(watchlist_face_detection_request_dto.old_face_detection_id)
        new_face_detection = self.uow.face_detection.get(watchlist_face_detection_request_dto.face_detection_id)

        detected_person = {
            "id": old_face_detection.id,
            "image_url": old_face_detection.image_url,
            "match_image_url": new_face_detection.image_url,
            "created_date": new_watchlist_face_detection.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "thread": True
        }
        self.detected_face_service.notify_detected_face(detected_person)

        return detected_person

    def get_all_watchlist(self, company_id: str) -> Optional[Dict]:
        """
        Get all watchlist for a company
        :param company_id
        """

        return self.uow.watchlist.get_watchlist_by_company_id(company_id)

    def get_all_watchlist_face_detections(self, company_id: str) -> list[dict]:
        """
        Get all watchlist for a company
        :param company_id
        """
        list_watchlist = self.uow.watchlist.get_watchlist_by_company_id(company_id)
        list_watchlist_ids = [item['id'] for item in list_watchlist]

        list_of_watchlist_face_detection \
            = self.uow.watchlist_face_detection.get_watchlist_face_detections(list_watchlist_ids)

        detected_persons = []

        for watchlist_face_detection in list_of_watchlist_face_detection:
            watchlist = self.uow.watchlist.get(watchlist_face_detection.watchlist_id)

            old_face_detection = self.uow.face_detection.get(watchlist.face_detection_id)

            match_face_detection = self.uow.face_detection.get(watchlist_face_detection.face_detection_id)

            detected_person = {
                "id": old_face_detection.id,
                "image_url": old_face_detection.image_url,
                "match_image_url": match_face_detection.image_url,
                "created_date": match_face_detection.created_date.strftime("%Y-%m-%d %H:%M:%S"),
                "thread": True
            }

            detected_persons.append(detected_person)

        return detected_persons
