from dataclasses import dataclass
from uuid import UUID


@dataclass
class Department:
    id: UUID

    name: str

    manager_user_id: UUID