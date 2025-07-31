from dataclasses import dataclass
from database.repositories.admins.base import AdminsRepo


@dataclass
class AdminsService:
    admins_repo: AdminsRepo
    
    async def get_admin(id: int):
        ...
    
    async def create_user():
        ...
        
    async def get_user_accounts(user_id: int):
        ...
        
    async def edit_user(user_id: int):
        ...
        
    async def delete_user(user_id: int):
        ...
        