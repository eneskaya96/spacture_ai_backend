from typing import Dict

from sqlalchemy import MetaData, Table, Column, DateTime, String, ForeignKey


from src.infrastructure.entities.face_detection.face_detection import FaceDetection
from src.infrastructure.mappings import BaseMapper


class FaceDetectionMapper(BaseMapper):
    def __init__(self, metadata: MetaData):
        super().__init__(metadata, FaceDetection)

    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        face_detection_mapping = Table(
            'face_detection', self._metadata,
            Column('id', String(250), primary_key=True),
            Column('company_id', String(250), ForeignKey('company.id'), nullable=False),
            Column('image_url', String(250), nullable=False),
            Column('created_date', DateTime, nullable=False),
            Column('modified_date', DateTime, nullable=True)
        )

        self.mapper_registry.map_imperatively(FaceDetection, face_detection_mapping)

