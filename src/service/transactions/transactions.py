from dataclasses import dataclass
from database.repositories.admins.base import AdminsRepo
from database.repositories.transactions.base import TransactionsRepo


@dataclass
class TransactionsService:
    transactions_repo: TransactionsRepo
    
    async def add_transaction():
        ...