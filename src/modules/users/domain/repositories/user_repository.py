from abc import ABC, abstractmethod
from uuid import UUID


class UserRepository(ABC):

    @abstractmethod
    async def get_by_id(self, user_id: UUID):
        pass

    @abstractmethod
    async def get_by_bale_id(self, bale_user_id: str):
        pass

    @abstractmethod
    async def create(self, user):
        pass