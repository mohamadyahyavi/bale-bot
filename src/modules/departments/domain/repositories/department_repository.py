from abc import ABC, abstractmethod
from uuid import UUID

from src.modules.departments.domain.entities.department import Department


class DepartmentRepository(ABC):

    @abstractmethod
    async def create(
        self,
        department: Department
    ) -> Department:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        department_id: UUID
    ) -> Department | None:
        pass

    @abstractmethod
    async def get_department_details(
        self,
        department_id: UUID
    ):
        """
        Returns:
        {
            "id": UUID,
            "name": str,

            "manager": {
                "id": UUID,
                "first_name": str,
                "last_name": str,
                "bale_user_id": str
            },

            "members": [
                {
                    "id": UUID,
                    "first_name": str,
                    "last_name": str,
                    "bale_user_id": str
                }
            ]
        }
        """
        pass

    @abstractmethod
    async def get_department_members(
        self,
        manager_user_id: UUID
    ):
        """
        Returns all users managed by a specific manager.
        """
        pass