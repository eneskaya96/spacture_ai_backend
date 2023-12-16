from typing import Dict

from sqlalchemy import MetaData, Table, Column, DateTime, String


from src.infrastructure.entities.company.company_rtsp_url import CompanyRTSPUrl
from src.infrastructure.mappings import BaseMapper


class CompanyRTSPUrlMapper(BaseMapper):
    def __init__(self, metadata: MetaData):
        super().__init__(metadata, CompanyRTSPUrl)

    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        company_rtsp_url_mapping = Table(
            'company_rtsp_url', self._metadata,
            Column('id', String(250), primary_key=True),
            Column('company_id', String(250), nullable=False),
            Column('rtsp_url', String(2500), nullable=False),
            Column('path', String(250), nullable=False),
            Column('created_date', DateTime, nullable=False),
            Column('modified_date', DateTime, nullable=True)
        )

        self.mapper_registry.map_imperatively(CompanyRTSPUrl, company_rtsp_url_mapping)

