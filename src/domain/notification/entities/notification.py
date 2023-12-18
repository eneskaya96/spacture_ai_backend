from __future__ import annotations

from src.domain.seed_work.model.base_entity_model import BaseStrEntityModel


class Notification(BaseStrEntityModel):
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
