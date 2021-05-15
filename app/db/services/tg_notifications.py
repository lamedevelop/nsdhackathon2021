from app.db.models.user import User
from app.db.schema import users_table, tg_notifications_table
from app.db.services.abstract import AbstractService


class TgNotificationsService(AbstractService):

    async def getUnfinishedNotifications(self):
        session = await self.get_session()
        res = session.query(tg_notifications_table) \
            .filter(tg_notifications_table.c.executed.in_([False])) \
            .all()

        notifications = []
        for message in res:
            notifications.append(message[0])
        return notifications

    async def checkUserExist(self, tg_id: int):
        user = await self.select(
            users_table.select().where(
                users_table.c.tg_id == tg_id
            )
        )

        if user:
            return User(**user)
        else:
            return False
