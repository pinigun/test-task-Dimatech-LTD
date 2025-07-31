from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DSN : str = 'postgresql+asyncpg://pguser:1029384756@localhost:5432/dimatech_db'
    
    
settings = Settings()