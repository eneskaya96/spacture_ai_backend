from typing import Optional, Dict, List, Type

from sqlalchemy import desc

from src.domain.watchlist.entities.watchlistFaceDetection import WatchlistFaceDetection as DomainWatchlistFaceDetection
from src.domain.watchlist.repositories.watchlist_face_detection_repository import WatchlistFaceDetectionRepository as WatchlistFaceDetectionDomainRepository
from src.infrastructure.entities.watchlist.watchlist_face_detection import WatchlistFaceDetection
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class WatchlistFaceDetectionRepository(BaseGenericRepository[DomainWatchlistFaceDetection], WatchlistFaceDetectionDomainRepository):

    def __init__(self) -> None:
        super().__init__(WatchlistFaceDetection, DomainWatchlistFaceDetection)

    def get_watchlist_face_detections(self, watchlist_ids: List[str], limit, offset) -> list[Type[WatchlistFaceDetection]]:
        return self.session.query(WatchlistFaceDetection)\
            .filter(WatchlistFaceDetection.watchlist_id.in_(watchlist_ids))\
            .order_by(desc(WatchlistFaceDetection.created_date))\
            .limit(limit) \
            .offset(offset) \
            .all()
