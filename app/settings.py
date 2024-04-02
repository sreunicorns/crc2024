from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "applications"
    APP_NAME: str = "CRC Applications"
    ECHO_SQL: bool = False
    DB_CONFIG: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
