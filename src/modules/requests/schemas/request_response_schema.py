from pydantic import BaseModel

from uuid import UUID

from datetime import datetime



class RequestResponseSchema(BaseModel):

    id: UUID

    user_id: UUID

    manager_id: UUID

    type: str

    status: str

    data: dict

    created_at: datetime | None


    class Config:

        from_attributes = True