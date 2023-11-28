import logging
from typing import Optional

from src.api.models.dto.company.company_request_dto import CompanyRequestDto
from src.domain.company.entities.company import Company
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
from src.services.base.base_service import BaseService


class CompanyService(BaseService):
    logger = logging.getLogger(__name__)

    def __init__(self, uow: Optional[UnitOfWork] = None) -> None:
        super().__init__(uow)

    def create_company(self, company_request_dto: CompanyRequestDto) -> Company:
        """
        Create a new company and returns it
        :param company_request_dto
        """

        new_company = Company.create_company(company_request_dto.name)

        with self.uow:
            self.uow.companies.insert(new_company)

        self.logger.info(f'Company {company_request_dto.name} is created')
        return new_company

    def get_company_by_id(self, company_id: str) -> Company:
        """
        Get company and returns it
        :param company_id
        """

        with self.uow:
            company = self.uow.companies.get(company_id)

        self.logger.info(f'Company is obtained by id: {company_id} ')
        return company
