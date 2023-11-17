from __future__ import annotations

from typing import List
from pydantic import BaseModel

from src.domain.watchlist.entities.watchlist import Watchlist


class WatchlistsResponseDto(BaseModel):
    company_id: str
    face_detection_id: str

    @classmethod
    def create(cls, watchlists: List[Watchlist]) -> List[WatchlistsResponseDto]:
        return [cls(
            company_id=watchlist.company_id,
            face_detection_id=watchlist.face_detection_id
        ) for watchlist in watchlists]