from pydantic import BaseModel
from uuid import UUID


class DepartmentManagerUpdate(BaseModel):

    manager_user_id: UUID