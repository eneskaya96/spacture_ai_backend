from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime

from src.infrastructure.entities.company.company import Company


class CompanyResponseDto(BaseModel):
    id: str
    name: str

    @classmethod
    def create(cls, company: Company) -> CompanyResponseDto:
        return cls(
            id=company.id,
            name=company.name,
        )
