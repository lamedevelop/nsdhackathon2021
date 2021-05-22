from typing import Optional

from pydantic import BaseModel, validator


class UserRegistration(BaseModel):
    first_name: str
    last_name: str
    password_hash: str
    phone: str
    email: str
    registration_date: int


class User(BaseModel):
    user_id: int
    tg_id: Optional[int]
    tg_authdate: Optional[int]
    tg_hash: Optional[str]
    last_auth: int
    last_update: int
