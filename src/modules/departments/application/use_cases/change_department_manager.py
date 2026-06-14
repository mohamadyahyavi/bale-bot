from uuid import UUID


class ChangeDepartmentManagerUseCase:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository


    async def execute(
        self,
        department_id: UUID,
        manager_user_id: UUID,
    ):


        # بررسی وجود دپارتمان
        department = await self.repository.get_by_id(
            department_id
        )


        if not department:
            raise ValueError(
                "Department not found"
            )


        return await (
            self.repository
            .update_manager(
                department_id,
                manager_user_id,
            )
        )