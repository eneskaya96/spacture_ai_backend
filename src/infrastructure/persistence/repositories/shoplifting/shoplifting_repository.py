from typing import Optional, List, Dict

from src.domain.shoplifting.entities.shoplifting import Shoplifting as DomainShoplifting
from src.domain.shoplifting.repositories.shoplifting_repository import ShopliftingRepository as ShopliftingDomianRepository
from src.infrastructure.entities.shoplifting.shoplifting import Shoplifting
from src.infrastructure.entities.face_detection.face_detection import FaceDetection
from src.infrastructure.persistence.repositories.base_repository import BaseGenericRepository


class ShopliftingRepository(BaseGenericRepository[DomainShoplifting], ShopliftingDomianRepository):

    def __init__(self) -> None:
        super().__init__(Shoplifting, DomainShoplifting)

    def get_by_face_detection_id(self, face_detection_id: str) -> Optional[Shoplifting]:
        return (self.session.query(Shoplifting)
                .filter(Shoplifting.face_detection_id == face_detection_id)
                .order_by(Shoplifting.created_date.desc())
                .first())

    def get_all_shoplifting_by_company_id(self, company_id: str) -> Optional[List[Dict]]:
        res = self.session.query(
            Shoplifting.company_id,
            Shoplifting.face_detection_id,
            Shoplifting.video_url,
            FaceDetection.image_url,
            FaceDetection.created_date) \
            .join(FaceDetection) \
            .filter(Shoplifting.company_id == company_id) \
            .filter(Shoplifting.face_detection_id == FaceDetection.id) \
            .all()
        result_dicts = [
            {
                'company_id': row[0],
                'id': row[1],
                'video_url': row[2],
                'image_url': row[3],
                'created_date': row[4]
            }
            for row in res
        ]
        return result_dicts