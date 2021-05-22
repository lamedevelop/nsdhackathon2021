import os
import zipfile

from fastapi import UploadFile

from app.db.models.message import Message
from app.db.schema import messages_table
from app.db.services.abstract import AbstractService


class MessagesService(AbstractService):

    files_dir = 'data'

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

    async def getMessage(self, message_id: int):
        message = await self.select(
            messages_table.select().where(
                messages_table.c.message_id == message_id
            )
        )
        if message:
            return Message(**message)
        else:
            return False

    async def getZipFileStruct(self, message_id):
        message = await self.getMessage(message_id)
        if message:
            zip_file = zipfile.ZipFile(message.filepath)
            return zip_file.namelist()
        else:
            pass

    async def filterMessages(self, query_result):
        messages = []
        for message in query_result:
            messages.append(Message(**message).dict())
        return messages

    def saveFile(self, file: UploadFile):
        try:
            file_name = os.getcwd() + self.files_dir + file.filename
            with open(file_name, 'wb+') as f:
                f.write(file.file.read())
                f.close()
            return True
        except Exception as e:
            return False
