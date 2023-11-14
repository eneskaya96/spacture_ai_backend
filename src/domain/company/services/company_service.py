import logging
from src.domain.company.entities.company import Company


class FortuneService:
    logger = logging.getLogger(__name__)

    @staticmethod
    def create_fortune(name: str) -> Company:
        return Company.create_company(name)
