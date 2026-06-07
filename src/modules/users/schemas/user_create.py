from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import date


class UserCreate(BaseModel):
    bale_user_id: str
    first_name: str
    last_name: str

    email: EmailStr | None = None
    mobile: str | None = None

    kimai_user_id: int

    department_id: UUID

    contract_start_date: date | None = None
    contract_end_date: date | None = None