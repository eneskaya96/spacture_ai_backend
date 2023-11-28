from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class NotifyFaceDetectionRequestDto(BaseModel):
    face_detection_id: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'face_detection_id': self.face_detection_id
        }
