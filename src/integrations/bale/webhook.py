from fastapi import APIRouter, Request

from integrations.bale.state.memory_state import MemoryState
from integrations.bale.handlers.request_handler import RequestHandler

from src.core.dependencies import get_create_request_usecase


router = APIRouter()


state = MemoryState()
usecase = get_create_request_usecase()
handler = RequestHandler(state, usecase)


@router.post("/bale/webhook")
async def bale_webhook(request: Request):

    update = await request.json()

    message = update["message"]

    user_id = message["from"]["id"]
    text = message["text"]



    step = state.get(user_id, "step")



    # start flow
    if text == "requests":
        return await handler.start(user_id)



    return await handler.handle(user_id, text) 