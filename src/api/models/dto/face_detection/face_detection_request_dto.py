from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class FaceDetectionRequestDto(BaseModel):
    company_id: str
    image_url: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'company_id': self.company_id,
            'image_url': self.image_url
        }
