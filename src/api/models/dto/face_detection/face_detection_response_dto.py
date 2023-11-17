from __future__ import annotations
from pydantic import BaseModel

from src.infrastructure.entities.face_detection.face_detection import FaceDetection


class FaceDetectionResponseDto(BaseModel):
    id: str
    company_id: str
    image_url: str

    @classmethod
    def create(cls, face_detection: FaceDetection) -> FaceDetectionResponseDto:
        return cls(
            id=face_detection.id,
            company_id=face_detection.company_id,
            image_url=face_detection.image_url,
        )
