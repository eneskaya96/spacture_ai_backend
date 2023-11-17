from __future__ import annotations
from pydantic import BaseModel

from src.infrastructure.entities.watchlist.watchlist_face_detection import WatchlistFaceDetection


class WatchlistFaceDetectionResponseDto(BaseModel):
    watchlist_id: str
    face_detection_id: str

    @classmethod
    def create(cls, watchlist_face_detection: WatchlistFaceDetection) -> WatchlistFaceDetectionResponseDto:
        return cls(
            watchlist_id=watchlist_face_detection.id,
            face_detection_id=watchlist_face_detection.face_detection_id
        )
