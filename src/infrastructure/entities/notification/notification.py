from __future__ import annotations

from dataclasses import dataclass
from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class Notification(BaseStrEntity):
    company_id: str
    token: str

    class Config:
        orm_mode = True

    @classmethod
    def create_notification_token(cls,
                                  company_id: str,
                                  token: str) -> Notification:
        return cls(company_id=company_id,
                   token=token)
