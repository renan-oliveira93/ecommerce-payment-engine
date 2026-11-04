from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    rabbitmq_url: str
    stripe_api_key: str
    stripe_webhook_secret: str
    otel_exporter_otlp_endpoint: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
