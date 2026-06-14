from requests.domain.entities.request import RequestEntity


from requests.domain.enums.request_enum import (
    RequestStatus
)



class CreateRequestUseCase:



    def __init__(

        self,

        request_repository,

        user_repository

    ):


        self.request_repository = request_repository


        self.user_repository = user_repository




    async def execute(


        self,

        bale_user_id: str,

        data


    ):



        user = await self.user_repository.find_by_bale_id(

            bale_user_id

        )



        if not user:

            raise Exception(
                "User not found"
            )



        manager_id = (

            user

            .department

            .manager_user_id

        )



        if not manager_id:

            raise Exception(
                "Manager not found"
            )



        request = RequestEntity(



            user_id=user.id,



            manager_id=manager_id,



            type=data.type,



            status=RequestStatus.PENDING,



            data=data.body

        )



        return await self.request_repository.create(

            request

        )