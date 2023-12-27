import abc
from typing import Optional, List

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.face_detection.entities.face_detection import FaceDetection


class FaceDetectionRepository(BaseRepository[FaceDetection], abc.ABC):
    @abc.abstractmethod
    def get_face_detection_by_company_id(self, company_id: str, limit: int, offset: int) -> Optional[List[FaceDetection]]:
        pass
