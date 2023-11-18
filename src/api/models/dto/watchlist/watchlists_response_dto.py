from __future__ import annotations

from typing import List
from pydantic import BaseModel
from datetime import datetime

from src.domain.watchlist.entities.watchlist import Watchlist


class WatchlistsResponseDto(BaseModel):
    id: str
    company_id: str
    face_detection_id: str
    image_url: str
    created_date: datetime

    @classmethod
    def create(cls, watchlist_data: list[dict]) -> list[WatchlistsResponseDto]:
        return [cls(**item) for item in watchlist_data]