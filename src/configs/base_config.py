import logging

from pydantic import Field, BaseSettings

from typing import Optional


class BaseConfig(BaseSettings):
    """Base Configuration"""

    ENVIRONMENT: Optional[str] = Field('local', env='ENVIRONMENT')

    GRAYLOG_IP: Optional[str]
    GRAYLOG_PORT: Optional[int]

    ENABLE_GRAYLOG: Optional[bool] = Field(True)
    GRAYLOG_LOGGING_LEVEL: int = Field(logging.INFO)
