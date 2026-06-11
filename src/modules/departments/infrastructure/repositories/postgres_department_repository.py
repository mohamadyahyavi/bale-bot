from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.departments.infrastructure.models.department_model import (
    DepartmentModel,
)


class PostgresDepartmentRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, department):

        db_department = DepartmentModel(
            name=department.name,
            manager_user_id=department.manager_user_id,
        )

        self.session.add(db_department)

        await self.session.commit()

        await self.session.refresh(db_department)

        return db_department

    async def get_by_id(self, department_id: UUID):

        stmt = select(DepartmentModel).where(
            DepartmentModel.id == department_id
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_by_name(self, name: str):

        stmt = select(DepartmentModel).where(
            DepartmentModel.name == name
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all(self):

        stmt = select(DepartmentModel)

        result = await self.session.execute(stmt)

        return result.scalars().all()

    async def update_manager(self, department_id: UUID, manager_user_id: UUID):

        department = await self.get_by_id(department_id)

        if not department:
            return None

        department.manager_user_id = manager_user_id

        await self.session.commit()

        await self.session.refresh(department)

        return department

    async def delete(self, department_id: UUID):

        department = await self.get_by_id(department_id)

        if not department:
            return False

        await self.session.delete(department)

        await self.session.commit()

        return True

    async def is_manager(self, user_id: UUID) -> bool:

        stmt = select(DepartmentModel.id).where(
            DepartmentModel.manager_user_id == user_id
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none() is not None