import abc
from typing import Optional, List, Dict

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.watchlist.entities.watchlist import Watchlist


class WatchlistRepository(BaseRepository[Watchlist], abc.ABC):
    @abc.abstractmethod
    def get_watchlist_by_company_id(self, company_id: str) -> Optional[Dict]:
        pass
