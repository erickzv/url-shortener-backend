from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_uri: str = "MONGO_URI"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
