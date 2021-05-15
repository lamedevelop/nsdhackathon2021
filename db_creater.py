import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection("localhost", "root", "User")

create_users = """
INSERT INTO
  `users` (`user_id`, `password_hash`, `phone`, `email`, `tg_id`, `tg_authdate`, `tg_hash`, `first_name`, `last_name`, `last_auth`, `last_update`, `registration_date`)
VALUES
  (0, '1234', '891045245', 'qq@gmail.com', 1, 2, 'some text', 'oleg', 'grinya', 3, 4, 5),
  (1, '1234', '891045535', 'ww@gmail.com', 6, 7, 'another text', 'kolyan', 'shkalka', 8, 9, 10),
  (2, '1234', '812045245', 'nn@gmail.com', 11, 12, 'right text', 'anzor', '???', 13, 14, 15),
  (3, '1234', '246742188', 'bb@gmail.com', 16, 17, 'left text', 'ilya', 'zemlya', 18, 19, 20),
"""

create_messages = """
INSERT INTO
  `messages` (`sender_id`, `receiver_id`, `message`, `filepath`, `creation_date`, `viewed`)
VALUES
  (0, 1, 'this is testing', 21, 22, 0),
  (2, 3, 'this is fake', 23, 24, 0),
  (1, 2, 'fakefactorio', 25, 26, 0),
  (2, 3, 'lie', 27, 28, 1),
"""

create_tg_notifications = """
INSERT INTO
  `tg_notifications ` (`notification_id`, `tg_id`, `message`, `executed`, `execution_date`, `creation_date`)
VALUES
  (0, 'kekmarakek', 'this is testing', 0, 29, 30),
  (1, 'kekmarakek', 'this is fake', 0, 31, 32),
  (2, 'kekmarakek', 'fakefactorio', 1, 33, 34),
  (3, 'kekmarakek', 'lie',1, 35, 36),
"""
execute_query(connection, create_users)