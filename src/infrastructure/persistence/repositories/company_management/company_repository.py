from typing import Optional

from src.domain.company.entities.company import Company as DomainCompany
from src.domain.company.repositories.company_repository import CompanyRepository as CompanyDomainRepository
from src.infrastructure.entities.company.company import Company
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class CompanyRepository(BaseGenericRepository[DomainCompany], CompanyDomainRepository):

    def __init__(self) -> None:
        super().__init__(Company, DomainCompany)

    def get_company(self, offset: int) -> Optional[Company]:
        return self.query.offset(offset).first()
