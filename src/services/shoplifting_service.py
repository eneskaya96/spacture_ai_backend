import logging
from typing import Optional, List

from src.api.models.dto.face_detection.face_detection_request_dto import FaceDetectionRequestDto
from src.api.models.dto.shoplifting.shoplifting_detected_request_dto import ShopliftingDetectedRequestDto
from src.domain.shoplifting.entities.shoplifting import Shoplifting
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
from src.services.base.base_service import BaseService
from src.services.detected_images import DetectedFaceService


class ShopliftingService(BaseService):
    logger = logging.getLogger(__name__)

    def __init__(self, socketio, uow: Optional[UnitOfWork] = None) -> None:
        self.detected_face_service = DetectedFaceService(socketio)
        super().__init__(uow)

    def shoplifting_detected(self, shoplifting_request_dto: ShopliftingDetectedRequestDto) -> Shoplifting:
        """
        Shoplifting detected
        :param shoplifting_request_dto
        """

        shoplifting = Shoplifting.create_shoplifting(shoplifting_request_dto.company_id,
                                                     shoplifting_request_dto.face_detection_id,
                                                     shoplifting_request_dto.video_url,
                                                     )

        with self.uow:
            self.uow.shoplifting.insert(shoplifting)

        face_detection = self.uow.face_detection.get(shoplifting_request_dto.face_detection_id)

        self.logger.info(f'Face detection is obtained by id: {face_detection} ')

        detected_person = {
            "id": face_detection.id,
            "image_url": face_detection.image_url,
            "match_image_url": None,
            "created_date": face_detection.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "thread": True
        }

        self.detected_face_service.notify_detected_face(detected_person, face_detection.company_id)

        return shoplifting

    def get_shoplifting(self, face_detection_id: str) -> Shoplifting:
        """
        Shoplifting detected
        :param face_detection_id
        """

        shoplifting = self.uow.shoplifting.get_by_face_detection_id(face_detection_id)
        return shoplifting

    def get_all_shoplifting(self, company_id: str) -> Optional[List[Shoplifting]]:
        """
        Get all face detections for a company
        :param company_id
        """

        return self.uow.shoplifting.get_all_shoplifting_by_company_id(company_id)

