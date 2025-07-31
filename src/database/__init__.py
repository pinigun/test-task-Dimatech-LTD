from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import settings


# Асинхронный движок SQLAlchemy
engine = create_async_engine(settings.POSTGRES_DSN, echo=True)  # echo=True для логирования SQL

# Фабрика сессий
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    with async_session_maker() as session:
        yield session