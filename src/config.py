from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class SupabaseSettings(BaseModel):
    url: str = "invalid"
    api_key: str = "invalid"


class OpenaiSettings(BaseModel):
    api_key: str = "invalid"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        extra="ignore",
    )

    api_title: str = "Workshop"
    secret_key: str = "invalid"
    debug: bool = False

    supabase: SupabaseSettings = SupabaseSettings()
    open_ai: OpenaiSettings = OpenaiSettings()


settings = Settings()
