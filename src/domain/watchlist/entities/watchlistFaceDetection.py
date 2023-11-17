from __future__ import annotations

from src.domain.seed_work.model.base_entity_model import BaseStrEntityModel


class WatchlistFaceDetection(BaseStrEntityModel):
    watchlist_id: str
    face_detection_id: str

    class Config:
        orm_mode = True

    @classmethod
    def create_watchlist_face_detection(cls,
                                        watchlist_id: str,
                                        face_detection_id: str) -> WatchlistFaceDetection:
        return cls(watchlist_id=watchlist_id,
                   face_detection_id=face_detection_id)
