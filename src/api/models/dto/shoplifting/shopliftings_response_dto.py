from __future__ import annotations

from typing import Optional, Dict
from pydantic import BaseModel
from datetime import datetime


class ShopliftingsResponseDto(BaseModel):
    id: str
    company_id: str
    image_url: str
    video_url: str
    thread: bool = True
    created_date: datetime

    @classmethod
    def create(cls, shoplifting_data: Optional[Dict]) -> list[ShopliftingsResponseDto]:
        return [cls(**item) for item in shoplifting_data]