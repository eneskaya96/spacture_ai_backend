from __future__ import annotations

from dataclasses import dataclass
from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class Company(BaseStrEntity):
    name: str

    class Config:
        orm_mode = True

    @classmethod
    def create_company(cls,
                       name: str) -> Company:
        return cls(name=name)

