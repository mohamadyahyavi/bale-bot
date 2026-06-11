from uuid import UUID

from fastapi import  Depends
from sqlalchemy.ext.asyncio import AsyncSession


from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from src.modules.departments.schemas.department_create import (
    DepartmentCreate,
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
):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Create department not implemented yet",
    )


@router.get(
    "/",
    response_model=list[
        DepartmentResponse
    ],
)
async def get_departments():
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Get departments not implemented yet",
    )


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
)
async def get_department(
    department_id: UUID,
):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Get department not implemented yet",
    )


@router.patch("/{department_id}/manager")
async def change_department_manager(
    department_id: UUID,
):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Change manager not implemented yet",
    )

@router.get(
    "/{department_id}/users",
    response_model=list[
        UserResponse
    ],
)
async def get_department_users(
    department_id: UUID,
):
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Get department users not implemented yet",
    )