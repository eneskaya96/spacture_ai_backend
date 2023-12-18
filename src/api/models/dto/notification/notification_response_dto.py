from __future__ import annotations
from pydantic import BaseModel

from src.infrastructure.entities.notification.notification import Notification


class NotificationResponseDto(BaseModel):
    company_id: str
    token: str

    @classmethod
    def create(cls, notification: Notification) -> NotificationResponseDto:
        return cls(
            id=notification.id,
            company_id=notification.company_id,
            token=notification.token
        )
