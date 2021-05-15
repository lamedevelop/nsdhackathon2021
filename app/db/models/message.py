from pydantic import BaseModel, validator


class Message(BaseModel):
    sender_id: int
    receiver_id: int
    message: str
    filepath: str
    creation_date: int
    viewed: bool
