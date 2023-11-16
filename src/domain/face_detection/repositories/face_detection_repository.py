import abc
from typing import Optional

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.face_detection.entities.face_detection import FaceDetection


class FaceDetectionRepository(BaseRepository[FaceDetection], abc.ABC):
    @abc.abstractmethod
    def get_face_detection(self, offset: int) -> Optional[FaceDetection]:
        pass
