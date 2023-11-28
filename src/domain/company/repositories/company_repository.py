import abc
from typing import Optional

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.company.entities.company import Company


class CompanyRepository(BaseRepository[Company], abc.ABC):
    @abc.abstractmethod
    def get_company(self, offset: int) -> Optional[Company]:
        pass
