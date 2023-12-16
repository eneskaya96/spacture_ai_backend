from typing import Optional, List

from src.domain.face_detection.entities.face_detection import FaceDetection as DomainFaceDetection
from src.domain.face_detection.repositories.face_detection_repository import FaceDetectionRepository as FaceDetectionDomainRepository
from src.infrastructure.entities.face_detection.face_detection import FaceDetection
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class FaceDetectionRepository(BaseGenericRepository[DomainFaceDetection], FaceDetectionDomainRepository):

    def __init__(self) -> None:
        super().__init__(FaceDetection, DomainFaceDetection)

    def get_face_detection_by_company_id(self, company_id: str) -> Optional[List[FaceDetection]]:
        face_detections = self.session.query(FaceDetection).filter(FaceDetection.company_id == company_id).all()

        return [DomainFaceDetection.parse_obj(face_detection.__dict__) for face_detection in face_detections]
