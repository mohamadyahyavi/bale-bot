from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.infrastructure.models.user_model import UserModel


class PostgresUserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user):

        db_user = UserModel(
            
            bale_user_id=user.bale_user_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            mobile=user.mobile,
            kimai_user_id=user.kimai_user_id,
            department_id=user.department_id,
            contract_start_date=user.contract_start_date,
            contract_end_date=user.contract_end_date,
            is_active=user.is_active,
            total_leave_hours=user.total_leave_hours,

            access_level=user.access_level

        )

        self.session.add(db_user)

        await self.session.commit()

        await self.session.refresh(db_user)

        return db_user

    async def get_by_id(self, user_id: UUID):

        stmt = select(UserModel).where(
            UserModel.id == user_id
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_bale_id(self, bale_user_id: str):

        stmt = select(UserModel).where(
            UserModel.bale_user_id == bale_user_id
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()
    

    async def get_by_department_id(
        self,
        department_id: UUID
    ):

        stmt = select(
            UserModel
        ).where(
            UserModel.department_id == department_id
        )


        result = await self.session.execute(
            stmt
        )


        return result.scalars().all()
    


    async def get_all(self):

            stmt = select(UserModel)

            result = await self.session.execute(stmt)

            return result.scalars().all()
    
    
    
    async def update(
    self,
    user_id: UUID,
    data
    ):

        user = await self.get_by_id(
        user_id
        )


        if not user:
           return None


        update_data = data.model_dump(
               exclude_unset=True
        )


        for field, value in update_data.items():

            setattr(
            user,
            field,
            value
            )


        await self.session.commit()


        await self.session.refresh(
        user
        )

        return user
    
    