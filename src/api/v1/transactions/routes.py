from fastapi import APIRouter


router = APIRouter(
    prefix='/transactions',
    tags=['Transactions']
)


@router.post('/webhook')
async def login(
    transaction_id: str,
    account_id:     int,
    user_id:        int,
    amount:         float,
    signature:      str,
):
    ...
    
    