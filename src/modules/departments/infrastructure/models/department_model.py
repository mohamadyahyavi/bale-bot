from sqlalchemy import (
    Column,
    ForeignKey,
    String
)

from sqlalchemy.dialects.postgresql import UUID

import uuid
from src.db.base import Base
from sqlalchemy import Column

class DepartmentModel(Base):
    __tablename__ = "departments"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String(100),
        nullable=False
    )

    manager_user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )