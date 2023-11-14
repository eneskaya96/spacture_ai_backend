from pydantic import Field, BaseSettings

from typing import Optional


class BaseConfig(BaseSettings):
    """Base Configuration"""

    ENVIRONMENT: Optional[str] = Field('local', env='ENVIRONMENT')
