from dataclasses import dataclass

from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class Company(BaseStrEntity):
    name: str


