import logging
from typing import Optional

from src.api.models.dto.watchlist.watchlist_face_detection_request_dto import WatchlistFaceDetectionRequestDto
from src.api.models.dto.watchlist.watchlist_request_dto import WatchlistRequestDto
from src.domain.watchlist.entities.watchlist import Watchlist
from src.domain.watchlist.entities.watchlistFaceDetection import WatchlistFaceDetection
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
from src.services.base.base_service import BaseService


class WatchlistService(BaseService):
    logger = logging.getLogger(__name__)

    def __init__(self, socketio, uow: Optional[UnitOfWork] = None) -> None:
        self.socketio = socketio
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

        self.socketio.emit('new_watchlist', {'data': [new_watchlist.id]}, namespace='/')

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
            "id": "ID_" + str(old_face_detection.id),
            "image_url": old_face_detection.image_url,
            "match_image_url": new_face_detection.image_url,
            "detection_date": watchlist_face_detection.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "thread": True
        }

        self.socketio.emit('new_detection', {'data': [detected_person]}, namespace='/')

    def create_watchlist_face_detection(self, watchlist_face_detection_request_dto: WatchlistFaceDetectionRequestDto):
        """
        Create a new watchlist face detection and returns it
        :param watchlist_face_detection_request_dto
        """

        if not self.uow.watchlist.get(watchlist_face_detection_request_dto.watchlist_id):
            self.logger.error(
                f'Watchlist with id: {watchlist_face_detection_request_dto.watchlist_id} is not found on DB')

        if not self.uow.face_detection.get(watchlist_face_detection_request_dto.face_detection_id):
            self.logger.error(
                f'Face detection with id: {watchlist_face_detection_request_dto.face_detection_id} is not found on DB')

        new_watchlist_face_detection = WatchlistFaceDetection.create_watchlist_face_detection(
            watchlist_face_detection_request_dto.watchlist_id,
            watchlist_face_detection_request_dto.face_detection_id)

        with self.uow:
            self.uow.watchlist_face_detection.insert(new_watchlist_face_detection)

        self.logger.info(f'Watchlist face detection is created for  request: {watchlist_face_detection_request_dto}')

        return new_watchlist_face_detection
