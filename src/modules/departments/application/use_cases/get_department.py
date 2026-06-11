from uuid import UUID


class GetDepartmentUseCase:

    def __init__(self, repository):
        self.repository = repository

    async def execute(
        self,
        department_id: UUID
    ):
        
        department = await self.repository.get_by_id(
            department_id
        )


        if not department:
            raise ValueError(
                "Department not found"
            )


        return department 