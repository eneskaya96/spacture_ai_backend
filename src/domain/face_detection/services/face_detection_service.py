import logging
from src.domain.face_detection.entities.face_detection import FaceDetection


class FaceDetectionService:
    logger = logging.getLogger(__name__)

    @staticmethod
    def create_face_detection(company_id: str, image_url: str) -> FaceDetection:
        return FaceDetection.create_face_detection(company_id, image_url)
