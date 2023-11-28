from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class WatchlistFaceDetectionRequestDto(BaseModel):
    company_id: str
    old_face_detection_id: str
    face_detection_id: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'company_id': self.company_id,
            'old_face_detection_id': self.old_face_detection_id,
            'face_detection_id': self.face_detection_id
        }
