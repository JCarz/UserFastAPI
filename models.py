from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User (BaseModel):
    id: Optional[UUID] = uuid4()
    f_name: str
    l_name: str
    m_name: Optional[str]
    gender: Gender 
    roles: List[Role] 

class UserUpdateRequest(BaseModel):
    f_name: Optional[str]
    l_name: Optional[str]
    m_name: Optional[str]
    roles: Optional[List[Role]]