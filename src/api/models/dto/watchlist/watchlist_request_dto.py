from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class WatchlistRequestDto(BaseModel):
    company_id: str
    face_detection_id: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'company_id': self.company_id,
            'face_detection_id': self.face_detection_id
        }
