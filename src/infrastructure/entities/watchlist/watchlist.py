from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import relationship

from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class Watchlist(BaseStrEntity):
    company_id: str
    face_detection_id: str

    class Config:
        orm_mode = True

    @classmethod
    def create_watchlist(cls, company_id: str,
                         face_detection_id: str) -> Watchlist:
        return cls(company_id=company_id,
                   face_detection_id=face_detection_id)
