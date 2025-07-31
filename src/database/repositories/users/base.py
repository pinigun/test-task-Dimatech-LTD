from abc import ABC, abstractmethod


class UsersRepo(ABC):
    @abstractmethod
    async def create():
        ...
        
    @abstractmethod
    async def get():
        ...
        
    @abstractmethod
    async def get_all():
        ...
        
    @abstractmethod
    async def update():
        ...
        
    @abstractmethod
    async def delete():
        ...
        
    