from sqlalchemy import (
    Column,
    String,
    Boolean,
    Integer,
    Date,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.db.base import Base
from sqlalchemy import Column


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)

    bale_user_id = Column(String, unique=True, nullable=False)

    first_name = Column(String)
    last_name = Column(String)

    email = Column(
        String(255)
    )

    mobile = Column(
        String(20)
    )

    kimai_user_id = Column(Integer, unique=True, nullable=False)

    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=True
    )

    contract_start_date = Column(Date)

    contract_end_date = Column(Date)


    access_level = Column(
        String(20),
        nullable=False,
        default="EMPLOYEE",
    )


    # ======================
    # Leave
    # ======================

    total_leave_hours = Column(
        Integer,
        nullable=False,
        default=0,
    )


    is_active = Column(Boolean, default=True,nullable=False)