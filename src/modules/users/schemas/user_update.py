from datetime import date

from pydantic import BaseModel, EmailStr


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None

    email: EmailStr | None = None
    mobile: str | None = None

    contract_start_date: date | None = None
    contract_end_date: date | None = None

    is_active: bool | None = None