import uuid


from sqlalchemy import (
    Column,
    ForeignKey,
    DateTime,
    Enum
)


from sqlalchemy.dialects.postgresql import (
    UUID,
    JSONB
)


from sqlalchemy.sql import func


from database import Base


from requests.domain.enums.request_enum import (
    RequestType,
    RequestStatus
)



class RequestModel(Base):


    __tablename__ = "requests"



    id = Column(

        UUID(as_uuid=True),

        primary_key=True,

        default=uuid.uuid4

    )



    user_id = Column(

        UUID(as_uuid=True),

        ForeignKey("users.id"),

        nullable=False

    )



    manager_id = Column(

        UUID(as_uuid=True),

        ForeignKey("users.id"),

        nullable=False

    )



    type = Column(

        Enum(
            RequestType,
            name="request_type",
            create_type=False
        ),

        nullable=False

    )



    status = Column(

        Enum(
            RequestStatus,
            name="request_status",
            create_type=False
        ),

        default=RequestStatus.PENDING,

        nullable=False

    )



    data = Column(

        JSONB,

        nullable=False

    )



    created_at = Column(

        DateTime,

        server_default=func.now()

    )



    processed_at = Column(

        DateTime,

        nullable=True

    )