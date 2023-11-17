import abc
from typing import Optional

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.watchlist.entities.watchlistFaceDetection import WatchlistFaceDetection


class WatchlistFaceDetectionRepository(BaseRepository[WatchlistFaceDetection], abc.ABC):
    @abc.abstractmethod
    def get_watchlist(self, offset: int) -> Optional[WatchlistFaceDetection]:
        pass
