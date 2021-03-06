from app.db.models.tg_notification import TgNotification
from app.db.schema import tg_notifications_table
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
            notifications.append(notification.dict())
        return notifications

    async def deactivateNotification(self, notification):
        await self.execute(
            tg_notifications_table.update()
            .where(tg_notifications_table.c.notification_id == notification.notification_id)
            .values({'executed': True})
        )
