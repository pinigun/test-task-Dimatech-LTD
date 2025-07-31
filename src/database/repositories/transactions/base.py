from abc import ABC, abstractmethod


class TransactionsRepo(ABC):
    @abstractmethod
    async def create():
        ...
        
    @abstractmethod
    async def get():
        ...
        
    @abstractmethod
    async def get_all():
        ...
        
    