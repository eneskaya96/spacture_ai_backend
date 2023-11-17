import logging
from typing import Optional

from src.api.models.dto.face_detection.face_detection_request_dto import FaceDetectionRequestDto
from src.api.models.dto.watchlist.watchlist_request_dto import WatchlistRequestDto
from src.domain.watchlist.entities.watchlist import Watchlist
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
from src.services.base.base_service import BaseService
from src.services.detected_person_service import DetectedPersonService


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
            self.logger.error(f'Face detection id: {watchlist_request_dto.face_detection_id} is found on DB')

        new_watchlist = Watchlist.create_watchlist(watchlist_request_dto.company_id,
                                                   watchlist_request_dto.face_detection_id)

        with self.uow:
            self.uow.watchlist.insert(new_watchlist)

        self.logger.info(f'Watchlist detection is created for  request: {watchlist_request_dto}')

        self.socketio.emit('new_watchlist', {'data': [new_watchlist.id]}, namespace='/')

        return new_watchlist
