from pydantic import BaseModel
from typing import Any


class ErrorResponse(BaseModel):
    error: str
    detail: str = ""


class SuccessResponse(BaseModel):
    message: str
    data: Any = None
