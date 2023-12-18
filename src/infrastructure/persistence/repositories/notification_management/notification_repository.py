from typing import Optional, List

from src.domain.notification.entities.notification import Notification as DomainNotification
from src.domain.notification.repositories.notification_repository import NotificationRepository as NotificationDomainRepository
from src.infrastructure.entities.notification.notification import Notification
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class NotificationRepository(BaseGenericRepository[DomainNotification], NotificationDomainRepository):

    def __init__(self) -> None:
        super().__init__(Notification, DomainNotification)

    def get_tokens_by_company_id(self, company_id: str) -> Optional[List[Notification]]:
        return self.session.query(Notification).filter(Notification.company_id == company_id).all()

    def get_token(self, token: str) -> Optional[Notification]:
        return self.session.query(Notification).filter(Notification.token == token).one_or_none()