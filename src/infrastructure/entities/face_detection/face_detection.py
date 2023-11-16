from __future__ import annotations

from dataclasses import dataclass
from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class FaceDetection(BaseStrEntity):
    company_id: str
    image_url: str

    class Config:
        orm_mode = True

    @classmethod
    def create_face_detection(cls,
                              company_id: str,
                              image_url: str) -> FaceDetection:
        return cls(company_id=company_id,
                   image_url=image_url)
