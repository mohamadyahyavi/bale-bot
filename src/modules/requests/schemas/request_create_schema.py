from pydantic import BaseModel

from requests.domain.enums.request_enum import RequestType

class CreateRequestSchema(BaseModel):


    type: RequestType


    body: dict