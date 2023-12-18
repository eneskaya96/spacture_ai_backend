from typing import Dict

from sqlalchemy import MetaData, Table, Column, DateTime, String, ForeignKey

from src.infrastructure.entities.notification.notification import Notification
from src.infrastructure.mappings import BaseMapper


class NotificationMapper(BaseMapper):
    def __init__(self, metadata: MetaData):
        super().__init__(metadata, Notification)

    def perform_mapping(self, mappings: Dict[type, Table]) -> Table:
        notification_mapping = Table(
            'notification_token', self._metadata,
            Column('id', String(250), primary_key=True),
            Column('company_id', String(250), ForeignKey('company.id'), nullable=False),
            Column('token', String(250), nullable=False),
            Column('created_date', DateTime, nullable=False),
            Column('modified_date', DateTime, nullable=True)
        )

        self.mapper_registry.map_imperatively(Notification, notification_mapping)

