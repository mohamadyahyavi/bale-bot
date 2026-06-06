from uuid import UUID


class GetUserUseCase:

    def __init__(self, repository):
        self.repository = repository

    async def execute(self, user_id: UUID):
        return await self.repository.get_by_id(user_id)