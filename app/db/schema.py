from sqlalchemy import (
    Column, Enum as MariaEnum, Integer, Float,
    Boolean, MetaData, String, Table, Text,
)


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(column_0_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

messages_table = Table(
    'messages',
    metadata,
    Column('sender_id', Integer, primary_key=True),
    Column('receiver_id', Integer, nullable=False),
    Column('message', Text, nullable=False),
    Column('filepath', Text, nullable=False, default=0),
    Column('creation_date', Integer, nullable=True, default=0),
    Column('viewed', Boolean, nullable=True, default=-1),
)

tg_notifications_table = Table(
    'tg_notifications',
    metadata,
    Column('notification_id', Integer, primary_key=True),
    Column('tg_id', Integer, nullable=False),
    Column('message', Text, nullable=False),
    Column('executed', Boolean, nullable=False, default=0),
    Column('execution_date', Integer, nullable=True, default=0),
    Column('creation_date', Integer, nullable=True, default=-1),
)

users_table = Table(
    'users',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('password_hash', Text, nullable=False),
    Column('phone', String(255), nullable=False),
    Column('email', String(255), nullable=False, default=0),
    Column('tg_id', Integer, nullable=True, default=0),
    Column('tg_authdate', Integer, nullable=True, default=-1),
    Column('tg_hash', Text, primary_key=True),
    Column('first_name', String(255), nullable=False),
    Column('last_name', String(255), nullable=False),
    Column('last_auth', Integer, nullable=False, default=0),
    Column('last_update', Integer, nullable=True, default=0),
    Column('registration_date', Integer, nullable=True, default=-1)
)
