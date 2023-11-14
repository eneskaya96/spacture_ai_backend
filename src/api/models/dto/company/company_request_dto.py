from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class CompanyRequestDto(BaseModel):
    name: str

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'company': self.name
        }
