from uuid import UUID


class ListUsersByDepartmentUseCase:

    def __init__(
        self,
        user_repository
    ):
        self.user_repository = user_repository


    async def execute(
        self,
        department_id: UUID
    ):

        users = await (
            self.user_repository
            .get_by_department_id(
                department_id
            )
        )

        return users