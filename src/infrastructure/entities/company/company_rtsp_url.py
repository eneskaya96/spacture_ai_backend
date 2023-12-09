from __future__ import annotations

from dataclasses import dataclass
from src.infrastructure.entities.base_entity import BaseStrEntity


@dataclass
class CompanyRTSPUrl(BaseStrEntity):
    company_id: str
    rtsp_url: str
    path: str

    class Config:
        orm_mode = True

    @classmethod
    def create_company_rtsp_url(cls,
                                company_id: str,
                                rtsp_url: str,
                                path: str) -> CompanyRTSPUrl:
        return cls(company_id=company_id,
                   rtsp_url=rtsp_url,
                   path=path)
