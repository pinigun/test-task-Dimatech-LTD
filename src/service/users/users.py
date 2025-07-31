from dataclasses import dataclass
from database.repositories.admins.base import AdminsRepo
from database.repositories.transactions.base import TransactionsRepo


@dataclass
class UsersService:
    transactions_repo: TransactionsRepo
    
    async def get_user(id: int):
        ...