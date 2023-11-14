from datetime import datetime
from typing import Optional, Any, Dict
from uuid import uuid4

from pydantic import BaseModel, Field


class BaseEntityModel(BaseModel):
    created_date: datetime = Field(default_factory=datetime.utcnow)
    modified_date: Optional[datetime] = None

    class Config:
        orm_mode = True

    def to_orm(self) -> Dict[str, Any]:
        return self.dict()


class BaseStrEntityModel(BaseEntityModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    class Config:
        orm_mode = True


class BaseIntEntityModel(BaseEntityModel):
    id: int = 0

    class Config:
        orm_mode = True
