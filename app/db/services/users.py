from sqlalchemy import and_

from app.db.models.user import User, UserRegistration
from app.db.schema import users_table
from app.db.services.abstract import AbstractService


class UsersService(AbstractService):

    STATUS_AUTH_OK = 1
    STATUS_AUTH_FAILED = 0

    async def checkUserExist(self, tg_id: int):
        return await self.getUserByTgId(tg_id)

    async def getUserByTgId(self, tg_id: int):
        user = await self.select(
            users_table.select().where(
                users_table.c.tg_id == tg_id
            )
        )
        return await self.getUser(user)

    async def getUserByLogin(self, email: str, password_hash: str):
        user = await self.select(
            users_table.select().where(
                and_(
                    users_table.c.email == email,
                    users_table.c.password_hash == password_hash
                )
            )
        )
        return await self.getUser(user)

    async def getUser(self, user):
        if user:
            return User(**user)
        else:
            return False

    async def login(self, email: str, password_hash: str):
        user = await self.getUserByLogin(email, password_hash)
        if user:
            return self.STATUS_AUTH_OK
        else:
            return self.STATUS_AUTH_FAILED

    async def register(self, user: UserRegistration):
        try:
            await self.execute(
                users_table.insert().values({
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'password_hash': user.password_hash,
                    'registration_date': user.registration_date,
                    'email': user.email,
                    'phone': user.phone,
                })
            )
            return self.STATUS_AUTH_OK
        except Exception as e:
            print(e)
            return self.STATUS_AUTH_FAILED
