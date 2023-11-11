import abc
from typing import Dict

from sqlalchemy import Table, MetaData
from sqlalchemy.orm import registry

class BaseMapper(abc.ABC):
    mapper_registry = registry()

    def __init__(self, metadata: MetaData, entity_type: type):
        self._metadata = metadata
        self._entity_type = entity_type

    def map(self, mappings: Dict[type, Table]) -> Table:
        mapping = self.perform_mapping(mappings)

        mappings[self._entity_type] = mapping

        return mapping

    @abc.abstractmethod
    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        pass
