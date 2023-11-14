from typing import Optional

from src.infrastructure.persistence.repositories.unit_of_work import UnitOfWork


class BaseService:

    def __init__(self, uow: Optional[UnitOfWork] = None) -> None:
        self._uow: Optional[UnitOfWork] = uow

    @property
    def uow(self) -> UnitOfWork:
        if not self._uow:
            self._uow = UnitOfWork()
        return self._uow

