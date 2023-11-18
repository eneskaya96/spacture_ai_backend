from typing import Optional, Dict

from src.domain.watchlist.entities.watchlistFaceDetection import WatchlistFaceDetection as DomainWatchlistFaceDetection
from src.domain.watchlist.repositories.watchlist_face_detection_repository import WatchlistFaceDetectionRepository as WatchlistFaceDetectionDomainRepository
from src.infrastructure.entities.watchlist.watchlist_face_detection import WatchlistFaceDetection
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class WatchlistFaceDetectionRepository(BaseGenericRepository[DomainWatchlistFaceDetection], WatchlistFaceDetectionDomainRepository):

    def __init__(self) -> None:
        super().__init__(WatchlistFaceDetection, DomainWatchlistFaceDetection)

    def get_watchlist_face_detections(self, company_id: str) -> Optional[Dict]:
        pass
