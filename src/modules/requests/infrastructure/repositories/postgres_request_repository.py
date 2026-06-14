from sqlalchemy.ext.asyncio import AsyncSession
from requests.infrastructure.models.request_model import (
    RequestModel
)


from requests.domain.repositories.request_repository import (
    RequestRepository
)

class PostgresRequestRepository(
    RequestRepository
):


    def __init__(self, session):

        self.session = session



    async def create(
        self,
        request
    ):


        model = RequestModel(


            user_id=request.user_id,


            manager_id=request.manager_id,


            type=request.type,


            status=request.status,


            data=request.data

        )


        self.session.add(model)


        await self.session.commit()


        await self.session.refresh(model)


        return model