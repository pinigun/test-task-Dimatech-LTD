from abc import ABC, abstractmethod


class AccountsRepo(ABC):
    @abstractmethod
    async def create():
        ...
        
    @abstractmethod
    async def get():
        ...
        
    