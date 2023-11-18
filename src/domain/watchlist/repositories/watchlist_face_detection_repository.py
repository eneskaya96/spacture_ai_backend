import abc
from typing import Optional, Dict

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.watchlist.entities.watchlistFaceDetection import WatchlistFaceDetection


class WatchlistFaceDetectionRepository(BaseRepository[WatchlistFaceDetection], abc.ABC):
    @abc.abstractmethod
    def get_watchlist_face_detections(self, company_id: str) -> Optional[Dict]:
        pass
