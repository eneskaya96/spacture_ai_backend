from typing import Optional, List, Dict

from src.domain.watchlist.entities.watchlist import Watchlist as DomainWatchlist
from src.domain.watchlist.repositories.watchlist_repository import WatchlistRepository as WatchlistDomainRepository
from src.infrastructure.entities.watchlist.watchlist import Watchlist
from src.infrastructure.entities.face_detection.face_detection import FaceDetection
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class WatchlistRepository(BaseGenericRepository[DomainWatchlist], WatchlistDomainRepository):

    def __init__(self) -> None:
        super().__init__(Watchlist, DomainWatchlist)

    def get_watchlist_by_company_id(self, company_id: str) -> Optional[Dict]:
        res = self.session.query(
            Watchlist.id,
            Watchlist.company_id,
            Watchlist.face_detection_id,
            FaceDetection.image_url,
            FaceDetection.created_date) \
            .join(FaceDetection) \
            .filter(Watchlist.company_id == company_id) \
            .filter(Watchlist.face_detection_id == FaceDetection.id) \
            .all()
        print("res", res)
        result_dicts = [
            {
                'id': row[0],
                'company_id': row[1],
                'face_detection_id': row[2],
                'image_url': row[3],
                'created_date': row[4]
            }
            for row in res
        ]
        return result_dicts