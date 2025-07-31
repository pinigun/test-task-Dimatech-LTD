from sqlalchemy.ext.asyncio import AsyncSession
from .base import AdminsRepo


class AdminsRepoPostgres(AdminsRepo):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    