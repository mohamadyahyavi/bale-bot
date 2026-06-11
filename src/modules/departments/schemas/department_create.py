from uuid import UUID

from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    name: str

    manager_user_id: UUID