from __future__ import annotations

from dataclasses import dataclass
from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class Watchlist(BaseStrEntity):
    face_detection_id: str

    class Config:
        orm_mode = True

    @classmethod
    def create_watchlist(cls,
                         face_detection_id: str) -> Watchlist:
        return cls(face_detection_id=face_detection_id)
