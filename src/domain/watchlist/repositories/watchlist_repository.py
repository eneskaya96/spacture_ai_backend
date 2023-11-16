import abc
from typing import Optional

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.watchlist.entities.watchlist import Watchlist


class WatchlistRepository(BaseRepository[Watchlist], abc.ABC):
    @abc.abstractmethod
    def get_watchlist(self, offset: int) -> Optional[Watchlist]:
        pass
