from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies import get_db

from src.modules.users.schemas.user_create import UserCreate
from src.modules.users.schemas.user_update import UserUpdate

from src.modules.users.infrastructure.repositories.postgres_user_repository import PostgresUserRepository
from src.modules.users.application.use_cases.create_user import CreateUserUseCase
from src.modules.users.application.use_cases.get_user import GetUserUseCase

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/{user_id}")
async def get_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    repo = PostgresUserRepository(db)
    use_case = GetUserUseCase(repo)

    return await use_case.execute(user_id)

@router.post("/")
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):

    repo = PostgresUserRepository(db)
    use_case = CreateUserUseCase(repo)

    user = await use_case.execute(payload)

    return user    

@router.get("/")
async def list_users(db: AsyncSession = Depends(get_db)):

    repo = PostgresUserRepository(db)

    return await repo.get_all()

@router.put("/{user_id}")
async def update_user(
    user_id: UUID,
    payload: UserUpdate,
    db: AsyncSession = Depends(get_db)
):

    repo = PostgresUserRepository(db)

    return await repo.update(user_id, payload)



