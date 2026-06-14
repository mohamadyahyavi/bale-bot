from uuid import UUID

from fastapi import  Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.dependencies import get_db
from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from src.modules.departments.schemas.department_create import (
    DepartmentCreate,
)

from src.modules.departments.schemas.department_manager_update import (
    DepartmentManagerUpdate,
)

from src.modules.departments.application.use_cases.change_department_manager import (
    ChangeDepartmentManagerUseCase,
)

from src.modules.users.application.use_cases.list_users_by_department import (
    ListUsersByDepartmentUseCase,
)

from src.modules.users.infrastructure.repositories.postgres_user_repository import (
    PostgresUserRepository,
)
from src.modules.departments.infrastructure.repositories.postgres_department_repository import (
    PostgresDepartmentRepository,
)
from src.modules.departments.application.use_cases.create_department import (
    CreateDepartmentUseCase,
)

from src.core.dependencies import (
    get_create_department_use_case,
)

from src.modules.departments.schemas.department_response import (
    DepartmentResponse,
)

from src.modules.users.schemas.user_response import (
    UserResponse,
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)

@router.post(
    "/",
    response_model=DepartmentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_department(
    payload: DepartmentCreate,
    db: AsyncSession = Depends(get_db),
):

    repo = PostgresDepartmentRepository(
        db
    )


    use_case = CreateDepartmentUseCase(
        repo
    )


    return await use_case.execute(
        payload
    )



@router.patch(
    "/{department_id}/manager",
    response_model=DepartmentResponse
)
async def change_department_manager(
    department_id: UUID,
    payload: DepartmentManagerUpdate,
    db: AsyncSession = Depends(get_db),
):

    repo = PostgresDepartmentRepository(db)


    use_case = ChangeDepartmentManagerUseCase(
        repo
    )


    return await use_case.execute(
        department_id,
        payload.manager_user_id
    )

@router.get(
    "/{department_id}/users",
    response_model=list[UserResponse],
)
async def get_department_users(
    department_id: UUID,
    db: AsyncSession = Depends(get_db),
):

    repo = PostgresUserRepository(db)

    use_case = ListUsersByDepartmentUseCase(
        repo
    )

    return await use_case.execute(
        department_id
    )