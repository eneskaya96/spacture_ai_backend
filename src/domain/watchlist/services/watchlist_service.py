import logging
from src.domain.watchlist.entities.watchlist import Watchlist


class WatchlistService:
    logger = logging.getLogger(__name__)

    @staticmethod
    def create_watchlist(face_detection_id: str) -> Watchlist:
        return Watchlist.create_watchlist(face_detection_id)
