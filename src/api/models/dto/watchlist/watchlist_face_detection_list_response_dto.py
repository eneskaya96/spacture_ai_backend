from __future__ import annotations

from typing import Dict

from pydantic import BaseModel
from datetime import datetime


class WatchlistFaceDetectionListResponseDto(BaseModel):
    id: str
    image_url: str
    match_image_url: str
    created_date: datetime
    thread: bool

    @classmethod
    def create(cls, detected_persons: list[dict]) -> list[WatchlistFaceDetectionListResponseDto]:
        return [cls(**detected_person) for detected_person in detected_persons]
