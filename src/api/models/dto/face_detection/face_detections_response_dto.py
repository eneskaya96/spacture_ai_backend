from __future__ import annotations

from typing import List
from pydantic import BaseModel

from src.domain.face_detection.entities.face_detection import FaceDetection


class FaceDetectionsResponseDto(BaseModel):
    id: str
    company_id: str
    image_url: str

    @classmethod
    def create(cls, face_detections: List[FaceDetection]) -> List[FaceDetectionsResponseDto]:
        return [cls(
            id=face_detection.id,
            company_id=face_detection.company_id,
            image_url=face_detection.image_url
        ) for face_detection in face_detections]