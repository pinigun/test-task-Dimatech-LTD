from database.repositories.admins.base import AdminsRepo
from config import settings
from tools.jwt_tools import JWTTools


class AdminJwtAuthService:
    admins_repo:    AdminsRepo | None = None
    jwt_tools:      JWTTools = JWTTools(secret_key=settings.SECRET_KEY)
    
    
    async def login(
        email: str,
        password: str
    ):
        
        ...
        
    async def check_auth(token: str):
        ...