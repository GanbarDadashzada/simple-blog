from pydantic import BaseModel
from typing import Optional

class Registration(BaseModel):

    username: Optional[str]
    password: Optional[str]
    email: Optional[str]
    name: Optional[str]
    surname: Optional[str]


class Authorization(BaseModel):

    username: Optional[str]