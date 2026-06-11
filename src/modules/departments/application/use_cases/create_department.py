from src.modules.departments.domain.entities.department import (
    Department,
)


class CreateDepartmentUseCase:

    def __init__(self, repository):
        self.repository = repository

    async def execute(self, data):

        # جلوگیری از duplicate
        existing = await self.repository.get_by_name(
            data.name
        )

        if existing:
            raise ValueError("Department already exists")

        department = Department(
            name=data.name,
            manager_user_id=data.manager_user_id
        )

        return await self.repository.create(department)