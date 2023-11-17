from typing import Optional, List

from src.domain.watchlist.entities.watchlist import Watchlist as DomainWatchlist
from src.domain.watchlist.repositories.watchlist_repository import WatchlistRepository as WatchlistDomainRepository
from src.infrastructure.entities.watchlist.watchlist import Watchlist
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class WatchlistRepository(BaseGenericRepository[DomainWatchlist], WatchlistDomainRepository):

    def __init__(self) -> None:
        super().__init__(Watchlist, DomainWatchlist)

    def get_watchlist_by_company_id(self, company_id: str) -> Optional[List[Watchlist]]:
        return self.session.query(Watchlist).filter(Watchlist.company_id == company_id).all()
