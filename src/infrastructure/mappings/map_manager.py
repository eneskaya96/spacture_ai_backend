from typing import Dict

from sqlalchemy import MetaData
from sqlalchemy.schema import Table

from src.infrastructure.mappings.company.company_mapper import CompanyMapper
from src.infrastructure.mappings.face_detection.face_detection_mapper import FaceDetectionMapper
from src.infrastructure.mappings.watchlist.watchlist_mapper import WatchlistMapper


class MapManager:
    _metadata: MetaData = None
    _mappings: Dict[type, Table] = {}

    @classmethod
    def map_entities(cls) -> MetaData:
        cls._metadata = MetaData(schema='face_recognition')

        CompanyMapper(cls._metadata).map(cls._mappings)
        FaceDetectionMapper(cls._metadata).map(cls._mappings)
        WatchlistMapper(cls._metadata).map(cls._mappings)

        return cls._metadata
