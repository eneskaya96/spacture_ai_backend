from typing import Dict

from sqlalchemy import MetaData
from sqlalchemy.schema import Table

from src.infrastructure.mappings.company.company_mapper import CompanyMapper


class MapManager:
    _metadata: MetaData = None
    _mappings: Dict[type, Table] = {}

    @classmethod
    def map_entities(cls) -> MetaData:
        cls._metadata = MetaData(schema='face_recognition')

        CompanyMapper(cls._metadata).map(cls._mappings)

        return cls._metadata
