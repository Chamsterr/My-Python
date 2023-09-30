from pydantic import BaseModel
from datetime  import datetime


class OperationCreate(BaseModel):
    id: int
    operation_type: str
    item_name: str
    price: str
    date: datetime