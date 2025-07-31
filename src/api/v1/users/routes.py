from fastapi import APIRouter


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('/me')
async def get_me():
    ...
    
    
@router.get('/me/accounts')
async def get_me_accounts():
    ...
    
    
@router.get('/me/transactions')
async def get_me_transactions():
    ...
