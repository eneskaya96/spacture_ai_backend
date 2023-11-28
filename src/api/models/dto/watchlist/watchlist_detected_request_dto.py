from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class WatchlistDetectedRequestDto(BaseModel):
    watchlist_face_detection_id: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'watchlist_face_detection_id': self.watchlist_face_detection_id
        }
