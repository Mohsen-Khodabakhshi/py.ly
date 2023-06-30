from pydantic import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class MongoSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    db_name: str | None = "pyly"

    class Config:
        env_prefix = "MONGO_"


mongo_settings = MongoSettings()
