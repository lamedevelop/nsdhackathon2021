from pydantic import BaseModel, validator


class User(BaseModel):
    user_id: int
    password_hash: str
    phone: str
    email: str
    tg_id: int
    tg_authdate: int
    tg_hash: str
    first_name: str
    last_name: str
    last_auth: int
    last_update: int
    registration_date: int
