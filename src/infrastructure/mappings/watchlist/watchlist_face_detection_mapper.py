from typing import Dict

from sqlalchemy import MetaData, Table, Column, DateTime, String, ForeignKey


from src.infrastructure.entities.watchlist.watchlist_face_detection import WatchlistFaceDetection
from src.infrastructure.mappings import BaseMapper


class WatchlistFaceDetectionMapper(BaseMapper):
    def __init__(self, metadata: MetaData):
        super().__init__(metadata, WatchlistFaceDetection)

    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        watchlist_face_detection_mapping = Table(
            'watchlist_face_detection', self._metadata,
            Column('id', String(250), primary_key=True),
            Column('watchlist_id', String(250), ForeignKey('watchlist.id'), nullable=False),
            Column('face_detection_id', String(250), ForeignKey('face_detection.id'), nullable=False),
            Column('created_date', DateTime, nullable=False),
            Column('modified_date', DateTime, nullable=True)
        )

        self.mapper_registry.map_imperatively(WatchlistFaceDetection, watchlist_face_detection_mapping)

