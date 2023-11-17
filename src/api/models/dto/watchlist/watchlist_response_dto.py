from __future__ import annotations
from pydantic import BaseModel

from src.infrastructure.entities.watchlist.watchlist import Watchlist


class WatchlistResponseDto(BaseModel):
    company_id: str
    face_detection_id: str

    @classmethod
    def create(cls, watchlist: Watchlist) -> WatchlistResponseDto:
        return cls(
            id=watchlist.id,
            company_id=watchlist.company_id,
            face_detection_id=watchlist.face_detection_id
        )
