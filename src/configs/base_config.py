from pydantic import Field
from pydantic_settings import BaseSettings

from typing import Optional


class BaseConfig(BaseSettings):
    """Base Configuration"""

    ENVIRONMENT: Optional[str] = Field('local', env='ENVIRONMENT')
