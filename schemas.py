from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class ClientBase(BaseModel):
    address: Optional[str]
    email: Optional[EmailStr]
    first_name: str
    identify: str
    last_name: str
    phone: Optional[str]
    type_identify: constr(pattern='^(CC|NIT)$')

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int

    class Config:
        orm_mode = True
