from app.db.schema import messages_table
from app.db.services.abstract import AbstractService


class MessagesService(AbstractService):
    async def getNewMessages(self, user_id):
        session = await self.get_session()
        res = session.query(messages_table) \
            .filter(messages_table.c.receiver_id.in_([user_id])) \
            .filter(messages_table.c.viewed.in_([False])) \
            .all()
        return await self.filterMessages(res)

    async def getOutcomeMessages(self, user_id):
        session = await self.get_session()
        res = session.query(messages_table) \
            .filter(messages_table.c.sender_id.in_([user_id])) \
            .all()
        return await self.filterMessages(res)

    async def getIncomeMessages(self, user_id):
        session = await self.get_session()
        res = session.query(messages_table) \
            .filter(messages_table.c.receiver_id.in_([user_id])) \
            .filter(messages_table.c.viewed.in_([True])) \
            .all()
        return await self.filterMessages(res)

    async def filterMessages(self, query_result):
        messages = []
        for message in query_result:
            messages.append(message[0])
        return messages
