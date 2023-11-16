import logging
from src.domain.company.entities.company import Company


class CompanyService:
    logger = logging.getLogger(__name__)

    @staticmethod
    def create_company(name: str) -> Company:
        return Company.create_company(name)
