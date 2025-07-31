from fastapi import APIRouter, Body, Query


ADMINS_USERS_TAG = 'Admins.Users'
ADMINS_ME_TAG = 'Admins.Me'


router = APIRouter(
    prefix='/admins',
)


@router.get('/me', tags=[ADMINS_ME_TAG])
async def get_me():
    ...


@router.post('/users', tags=[ADMINS_USERS_TAG])
async def create_user(
    full_name:  str = Body(...),
    email:      str = Body(...),
    password:   str = Body(...)
):
    ...


@router.get('/users', tags=[ADMINS_USERS_TAG])
async def get_users(
    page:           int = Query(1, gt=0),
    per_page:       int = Query(10, gt=0),
):
    ...
    

@router.get('/users/{user_id}/accounts', tags=[ADMINS_USERS_TAG])
async def get_users(
    user_id: int,
):
    ...
    
@router.get('/users/{user_id}/transactions', tags=[ADMINS_USERS_TAG])
async def get_users(
    user_id: int,
):
    ...
    
    
@router.patch('/users/{user_id}', tags=[ADMINS_USERS_TAG])
async def update_user(
    user_id:    int,
    full_name:  str | None = Body(None),
    email:      str | None = Body(None),
    password:   str | None = Body(None),
):
    ...


@router.delete('/users/{user_id}', tags=[ADMINS_USERS_TAG])
async def delete_user(user_id: int):
    ...