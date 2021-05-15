from app.db.models.tg_notification import TgNotification
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
            notification = TgNotification(**message)
            # todo: return after notification tests
            # await self.deactivateNotification(TgNotification(**message))
            notifications.append(notification.json())
        return notifications

    async def deactivateNotification(self, notification):
        await self.execute(
            tg_notifications_table.update()
            .where(tg_notifications_table.c.notification_id == notification.notification_id)
            .values({'executed': True})
        )

    async def checkUserExist(self, tg_id: int):
        return await self.getUserByTgId(tg_id)

    async def getUserByTgId(self, tg_id: int):
        user = await self.select(
            users_table.select().where(
                users_table.c.tg_id == tg_id
            )
        )
        return await self.getUser(user)

    async def getUser(self, user):
        if user:
            return User(**user)
        else:
            return False
