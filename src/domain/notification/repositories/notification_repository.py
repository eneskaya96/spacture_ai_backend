import abc
from typing import Optional, List

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.notification.entities.notification import Notification


class NotificationRepository(BaseRepository[Notification], abc.ABC):
    @abc.abstractmethod
    def get_tokens_by_company_id(self, company_id: str) -> Optional[List[Notification]]:
        pass

    @abc.abstractmethod
    def get_token(self, token: str) -> Optional[Notification]:
        pass