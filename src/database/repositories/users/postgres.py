from sqlalchemy.ext.asyncio import AsyncSession
from .base import UserRepo


class UsersRepoPostgres(UserRepo):
    def __init__(self, session: AsyncSession):
        self.session = session