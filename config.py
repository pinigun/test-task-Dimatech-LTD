from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DSN : PostgresDsn = 'asyncpg+postgres://postgres:postgers@localhost:5432/dimatech_db'
    
    
    
settings = Settings()