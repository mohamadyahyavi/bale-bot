from fastapi import APIRouter, Depends
from src.core.dependencies import get_db
from src.modules.requests.schemas.request_create_schema import CreateRequestSchema
from src.modules.requests.schemas.request_response_schema import RequestResponseSchema
from src.modules.requests.application.use_cases.create_request import CreateRequestUseCase
from src.modules.requests.infrastructure.repositories.postgres_request_repository import PostgresRequestRepository

router = APIRouter(
    prefix="/requests",
    tags=["Requests"]
)


@router.post(
    "/create",
    response_model=RequestResponseSchema
)
async def create_request(
    body: CreateRequestSchema,
    bale_user_id: str = Depends(get_current_bale_user),
    use_case: CreateRequestUseCase = Depends(get_create_request_usecase)
):
    result = await use_case.execute(
        bale_user_id,
        body
    )

    return result