import abc
from typing import Optional, List, Dict

from src.domain.seed_work.repository.base_repository import BaseRepository
from src.domain.shoplifting.entities.shoplifting import Shoplifting


class ShopliftingRepository(BaseRepository[Shoplifting], abc.ABC):
    @abc.abstractmethod
    def get_by_face_detection_id(self, face_detection_id: str) -> Optional[Shoplifting]:
        pass

    @abc.abstractmethod
    def get_all_shoplifting_by_company_id(self, company_id: str, limit: int, offset: int) -> Optional[List[Dict]]:
        pass
