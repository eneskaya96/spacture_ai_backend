import abc
from typing import Optional, Dict, List, Type

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.watchlist.entities.watchlistFaceDetection import WatchlistFaceDetection


class WatchlistFaceDetectionRepository(BaseRepository[WatchlistFaceDetection], abc.ABC):
    @abc.abstractmethod
    def get_watchlist_face_detections(self, watchlist_ids: List[str]) -> list[Type[WatchlistFaceDetection]]:
        pass
