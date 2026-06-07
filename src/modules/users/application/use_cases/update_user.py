from uuid import UUID


class UpdateUserUseCase:

    def __init__(self, repository):
        self.repository = repository

    async def execute(self, user_id: UUID, data):
        return await self.repository.update(user_id, data)