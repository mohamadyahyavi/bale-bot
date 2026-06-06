from uuid import uuid4

from src.modules.users.domain.entities.user import User


class CreateUserUseCase:

    def __init__(self, repository):
        self.repository = repository

    async def execute(self, data):

        user = User(
            id=uuid4(),
            bale_user_id=data.bale_user_id,
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            mobile=data.mobile,
            kimai_user_id=data.kimai_user_id,
            department_id=data.department_id,
            contract_start_date=data.contract_start_date,
            contract_end_date=data.contract_end_date,
            is_active=True
        )

        return await self.repository.create(user)