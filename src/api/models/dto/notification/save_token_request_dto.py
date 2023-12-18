from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class SaveTokenRequestDto(BaseModel):
    company_id: str
    token: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'company_id': self.company_id,
            'token': self.token
        }
