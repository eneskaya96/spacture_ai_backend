from __future__ import annotations
from pydantic import BaseModel

from src.infrastructure.entities.shoplifting.shoplifting import Shoplifting


class ShopliftingResponseDto(BaseModel):
    id: str
    company_id: str
    face_detection_id: str
    video_url: str

    @classmethod
    def create(cls, shoplifting: Shoplifting) -> ShopliftingResponseDto:
        return cls(
            id=shoplifting.id,
            company_id=shoplifting.company_id,
            face_detection_id=shoplifting.face_detection_id,
            video_url=shoplifting.video_url,
        )
