from uuid import UUID


class GetUserUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository


    async def execute(
        self,
        user_id: UUID
    ):

        user = await self.repository.get_by_id(
            user_id
        )


        if not user:
            raise ValueError(
                "User not found"
            )


        return user