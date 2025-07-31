from sqlalchemy.ext.asyncio import AsyncSession
from .base import TransactionsRepo


class TransactionsRepoPostgres(TransactionsRepo):
    def __init__(self, session: AsyncSession):
        self.session = session