from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class WatchlistFaceDetectionRequestDto(BaseModel):
    watchlist_id: str
    face_detection_id: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'watchlist_id': self.watchlist_id,
            'face_detection_id': self.face_detection_id
        }
