from __future__ import annotations

from src.domain.seed_work.model.base_entity_model import BaseStrEntityModel


class FaceDetection(BaseStrEntityModel):
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
