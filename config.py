from typing import List

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env")
    browsers: List[str]
    headless: bool
    app_url_no_str:HttpUrl

    @property
    def app_url(self) -> str:
        return str(self.app_url_no_str)
settings=Settings()