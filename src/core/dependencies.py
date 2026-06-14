from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.core.database import AsyncSessionLocal
from src.shared.authorization.access_service import (
    AccessService,
)
from src.modules.departments.infrastructure.repositories.postgres_department_repository import (
    PostgresDepartmentRepository,
)

from src.modules.departments.application.use_cases.create_department import (
    CreateDepartmentUseCase,
)

from src.modules.requests.infrastructure.repositories.request_repository import RequestRepository
from src.modules.requests.application.use_cases.create_request import CreateRequestUseCase

async def get_db() -> AsyncSession:

    async with AsyncSessionLocal() as session:
        yield session



def get_access_service(
    session,
):
    department_repository = (
        get_department_repository(
            session
        )
    )

    return AccessService(
        department_repository
    )

def get_department_repository(
    session : AsyncSession,
):
    return PostgresDepartmentRepository(
        session=session
    )

def get_create_department_use_case(
    session: AsyncSession,
):
    repository = get_department_repository(session)

    return CreateDepartmentUseCase(
        repository=repository
    )


def get_request_repository(session=Depends(get_db)):

    return RequestRepository(session)