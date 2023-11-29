import logging
from src.domain.shoplifting.entities.shoplifting import Shoplifting


class ShopliftingService:
    logger = logging.getLogger(__name__)

    @staticmethod
    def create_shoplifting(company_id: str, face_detection_id: str, video_url: str) -> Shoplifting:
        return Shoplifting.create_shoplifting(company_id, face_detection_id, video_url)
