from __future__ import annotations

from src.domain.seed_work.model.base_entity_model import BaseStrEntityModel


class Watchlist(BaseStrEntityModel):
    face_detection_id: str

    class Config:
        orm_mode = True

    @classmethod
    def create_watchlist(cls,
                         face_detection_id: str) -> Watchlist:
        return cls(face_detection_id=face_detection_id)
