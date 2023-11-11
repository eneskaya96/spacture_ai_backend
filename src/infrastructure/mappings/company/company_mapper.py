from typing import Dict

from sqlalchemy import MetaData, Table, Column, Integer, DateTime, String


from src.infrastructure.entities.company.company import Company
from src.infrastructure.mappings import BaseMapper



class CompanyMapper(BaseMapper):
    def __init__(self, metadata: MetaData):
        super().__init__(metadata, Company)

    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        company_mapping = Table(
            'fortune', self._metadata,
            Column('id', Integer, primary_key=True),
            Column('created_date', DateTime, nullable=False),
            Column('modified_date', DateTime),
            Column('name', String(250), nullable=False)
        )

        self.mapper_registry.map_imperatively(Company, company_mapping)

