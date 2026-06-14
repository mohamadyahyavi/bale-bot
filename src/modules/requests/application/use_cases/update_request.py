from datetime import datetime


class UpdateRequestStatusUseCase:


    def __init__(
        self,
        request_repository
    ):
        self.request_repository = request_repository



    async def execute(

        self,

        request_id,

        manager_id,

        data

    ):


        request = await self.request_repository.get_by_id(
            request_id
        )


        if not request:

            raise Exception(
                "Request not found"
            )



        if request.manager_id != manager_id:

            raise Exception(
                "Permission denied"
            )



        request.status = data.status


        request.processed_at = datetime.utcnow()



        return await self.request_repository.update(
            request
        )