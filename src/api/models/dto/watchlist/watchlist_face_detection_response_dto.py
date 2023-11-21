from __future__ import annotations

from typing import Dict

from pydantic import BaseModel
from datetime import datetime


class WatchlistFaceDetectionResponseDto(BaseModel):
    id: str
    image_url: str
    match_image_url: str
    created_date: datetime
    thread: bool

    @classmethod
    def create(cls, detected_person: Dict) -> WatchlistFaceDetectionResponseDto:
        return cls(
            id=detected_person.get('id', ''),
            image_url=detected_person.get('image_url', ''),
            match_image_url=detected_person.get('match_image_url', ''),
            created_date=detected_person.get('created_date', datetime.now()),
            thread=detected_person.get('thread', False)
        )
