from pydantic import BaseModel

from requests.domain.enums.request_enum import RequestStatus


class UpdateRequestStatusSchema(BaseModel):

    status: RequestStatus