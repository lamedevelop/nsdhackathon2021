from pydantic import BaseModel, validator


class TgNotification(BaseModel):
    notification_id: int
    tg_id: int
    message: str
    executed: bool
    execution_date: int
    creation_date: int
