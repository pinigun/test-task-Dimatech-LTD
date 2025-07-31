from fastapi import APIRouter


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post('/login')
async def login(
    email:      str,
    passwords:  str,
):
    ...


@router.post('/admin/login')
async def admin_login(
    email:      str,
    passwords:  str,
):
    ...
    
    