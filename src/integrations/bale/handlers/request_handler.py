from integrations.bale.flows.request_flow import RequestFlow


class RequestHandler:

    def __init__(self, state, usecase):

        self.state = state
        self.usecase = usecase
        self.flow = RequestFlow(state)


    async def start(self, user_id):

        self.state.set(user_id, "step", "SELECT_TYPE")

        return "نوع درخواست را انتخاب کنید"


    async def handle(self, user_id, text):

        step = self.state.get(user_id, "step")



        if text == "LEAVE":
            return await self.flow.start_leave(user_id)


        if text == "MISSION":
            return await self.flow.start_mission(user_id)



        if step == "LEAVE_TYPE":
            return await self.flow.leave_type(user_id, text)


        if step == "LEAVE_DATES":
            return await self.flow.leave_dates(user_id, text, self.usecase)


        if step == "MISSION_LOCATION":
            return await self.flow.mission_location(user_id, text)


        if step == "MISSION_DATES":
            return await self.flow.mission_dates(user_id, text)


        if step == "MISSION_DESCRIPTION":
            return await self.flow.mission_description(user_id, text, self.usecase)


        return "دستور نامشخص ❌"