import logging
from typing import Optional, List

from src.api.models.dto.face_detection.face_detection_request_dto import FaceDetectionRequestDto
from src.domain.face_detection.entities.face_detection import FaceDetection
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
from src.services.base.base_service import BaseService
from src.services.detected_images import DetectedFaceService


class FaceDetectionService(BaseService):
    logger = logging.getLogger(__name__)

    def __init__(self, socketio, uow: Optional[UnitOfWork] = None) -> None:
        self.detected_face_service = DetectedFaceService(socketio)
        super().__init__(uow)

    def notify_face_detected(self, face_detection_id: str) -> FaceDetection:
        """
        Notify face detected
        :param face_detection_id
        """

        face_detection = self.uow.face_detection.get(face_detection_id)

        self.logger.info(f'Face detection is obtained by id: {face_detection_id} ')

        detected_person = {
            "id": face_detection.id,
            "image_url": face_detection.image_url,
            "match_image_url": None,
            "created_date": face_detection.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "thread": False
        }

        self.detected_face_service.notify_detected_face(detected_person)

        return face_detection

    def create_face_detection(self, face_detection_request_dto: FaceDetectionRequestDto) -> FaceDetection:
        """
        Create a new face detection and returns it
        :param face_detection_request_dto
        """

        new_face_detection = FaceDetection.create_face_detection(face_detection_request_dto.company_id,
                                                                 face_detection_request_dto.image_url)

        with self.uow:
            self.uow.face_detection.insert(new_face_detection)

        self.logger.info(f'Face detection {face_detection_request_dto.image_url} is created')
        return new_face_detection

    def get_face_detections(self, company_id: str) -> Optional[List[FaceDetection]]:
        """
        Get all face detections for a company
        :param company_id
        """
        with self.uow:
            face_detections = self.uow.face_detection.get_face_detection_by_company_id(company_id)
        return face_detections
