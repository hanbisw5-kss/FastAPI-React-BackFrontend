# from pydantic_settings import BaseSettings
# from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os
DOTENV = os.path.join(os.path.dirname(__file__), ".env")

class Db_Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    model_config = SettingsConfigDict(env_file=DOTENV)
    # model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

@lru_cache()
def get_settings():
    return Db_Settings()
