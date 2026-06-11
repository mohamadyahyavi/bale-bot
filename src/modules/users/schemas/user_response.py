from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import date

class UserResponse(BaseModel):
    id: UUID

    bale_user_id: str

    first_name: str
    last_name: str

    email: EmailStr | None
    mobile: str | None

    department_id: UUID

    kimai_user_id: int

    contract_start_date: date | None
    contract_end_date: date | None

    is_active: bool

    class Config:
        from_attributes = True