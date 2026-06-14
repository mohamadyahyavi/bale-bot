from dataclasses import dataclass
from uuid import UUID
from datetime import date


@dataclass
class User:

    bale_user_id: str
    first_name: str
    last_name: str
    kimai_user_id: int
    department_id: UUID
    email: str | None
    mobile: str | None
    contract_start_date: date | None
    contract_end_date: date | None
    is_active: bool
    total_leave_hours: int = 0

    access_level: str = "EMPLOYEE"
    id: UUID | None=None