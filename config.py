from pathlib import Path
from typing import List
from pydantic import HttpUrl, field_validator, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class TestUser(BaseModel):
    email: str
    password: str
    username: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )

    browsers: List[str]
    headless: bool
    app_url_no_str: HttpUrl
    input_file: Path
    tracing_path: Path
    record_video_dir: Path
    test_user: TestUser
    allure_results_dir: Path

    def create_environment(self):
        items = [f'{key}={value}' for key, value in self.model_dump().items()]
        properties = '\n'.join(items)
        env_path = self.allure_results_dir / "environment.properties"
        env_path.write_text(properties, encoding="utf-8")

    @property
    def app_url(self) -> str:
        return str(self.app_url_no_str)

    @field_validator("input_file")
    def validate_file(cls, value: Path) -> Path:
        if not value.exists():
            value.parent.mkdir(parents=True, exist_ok=True)
            value.write_text("123", encoding="utf-8")
        return value

    @field_validator("tracing_path", "record_video_dir", "allure_results_dir")
    def validate_path(cls, value: Path) -> Path:
        if not value.exists():
            value.mkdir(parents=True, exist_ok=True)
        return value

settings = Settings()
settings.create_environment()

