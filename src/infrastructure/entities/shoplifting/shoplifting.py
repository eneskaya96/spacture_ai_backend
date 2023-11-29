from __future__ import annotations

from dataclasses import dataclass

from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class Shoplifting(BaseStrEntity):
    company_id: str
    face_detection_id: str
    video_url: str

    class Config:
        orm_mode = True

    @classmethod
    def create_shoplifting(cls,
                           company_id: str,
                           face_detection_id: str,
                           video_url: str) -> Shoplifting:
        return cls(company_id=company_id,
                   face_detection_id=face_detection_id,
                   video_url=video_url)
