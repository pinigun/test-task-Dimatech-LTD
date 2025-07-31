from database.repositories.users.base import UsersRepo
from tools.jwt_tools import JWTTools
from config import settings


class UserJwtAuthService:
    users_repo:     UsersRepo | None = None
    jwt_tools:      JWTTools = JWTTools(secret_key=settings.SECRET_KEY)
    
    async def login(
        email: str,
        password: str
    ):
        ...
        
    async def check_auth(token: str):
        ...
        