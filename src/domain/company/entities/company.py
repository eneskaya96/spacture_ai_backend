from __future__ import annotations

from src.domain.seed_work.model.base_entity_model import BaseStrEntityModel


class Company(BaseStrEntityModel):
    name: str

    class Config:
        orm_mode = True

    @classmethod
    def create_company(cls,
                       name: str) -> Company:
        return cls(name=name)
