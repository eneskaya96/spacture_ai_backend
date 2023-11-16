from typing import Optional

from src.domain.face_detection.entities.face_detection import FaceDetection as DomainFaceDetection
from src.domain.face_detection.repositories.face_detection_repository import FaceDetectionRepository as FaceDetectionDomainRepository
from src.infrastructure.entities.face_detection.face_detection import FaceDetection
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class FaceDetectionRepository(BaseGenericRepository[DomainFaceDetection], FaceDetectionDomainRepository):

    def __init__(self) -> None:
        super().__init__(FaceDetection, DomainFaceDetection)

    def get_face_detection(self, offset: int) -> Optional[FaceDetection]:
        pass
