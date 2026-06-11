from uuid import UUID

from pydantic import BaseModel


class DepartmentResponse(
    BaseModel
):
    
    name: str

    manager_user_id: UUID