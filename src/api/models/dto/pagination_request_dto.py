from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class PaginationRequestDto(BaseModel):
    limit: int
    offset: int

    def dict(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return {
            'limit': self.limit,
            'offset': self.offset
        }
