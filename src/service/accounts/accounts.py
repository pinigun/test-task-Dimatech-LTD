from dataclasses import dataclass
from database.repositories.accounts.base import AccountsRepo


@dataclass
class AccountsService:
    accounts_repo: AccountsRepo
    
    async def get_account(id: int):
        ...
    
    async def create_account():
        ...