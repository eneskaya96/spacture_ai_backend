from typing import Dict

from sqlalchemy import MetaData, Table, Column, DateTime, String, ForeignKey

from src.infrastructure.entities.watchlist.watchlist import Watchlist
from src.infrastructure.mappings import BaseMapper


class WatchlistMapper(BaseMapper):
    def __init__(self, metadata: MetaData):
        super().__init__(metadata, Watchlist)

    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        watchlist_mapping = Table(
            'watchlist', self._metadata,
            Column('id', String(250), primary_key=True),
            Column('company_id', String(250), ForeignKey('company.id'), nullable=False),
            Column('face_detection_id', String(250), ForeignKey('face_detection.id'), nullable=False),
            Column('created_date', DateTime, nullable=False),
            Column('modified_date', DateTime, nullable=True)
        )

        self.mapper_registry.map_imperatively(Watchlist, watchlist_mapping)

