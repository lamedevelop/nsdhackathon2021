CREATE DATABASE common;
USE common;

CREATE TABLE users (
    user_id int,
    password_hash text,
    phone varchar(255),
    email varchar(255),
    tg_id int,
    tg_authdate int,
    tg_hash text,
    first_name varchar(255),
    last_name varchar(255),
    last_auth int,
    last_update int,
    registration_date int
);

CREATE TABLE messages (
    sender_id int,
    receiver_id int,
    message text,
    filepath text,
    creation_date int,
    viewed bool
);

CREATE TABLE tg_notifications (
    notification_id int,
    tg_id int,
    message text,
    executed bool,
    execution_date int,
    creation_date int
);

INSERT INTO
  `users` (`user_id`, `password_hash`, `phone`, `email`, `tg_id`, `tg_authdate`, `tg_hash`, `first_name`, `last_name`, `last_auth`, `last_update`, `registration_date`)
VALUES
  (0, '1234', '891045245', 'qq@gmail.com', 122031432, 2, 'some text', 'oleg', 'grinya', 3, 4, 5),
  (1, '1234', '891045535', 'ww@gmail.com', 297002761, 7, 'another text', 'kolyan', 'shkalka', 8, 9, 10),
  (2, '1234', '812045245', 'nn@gmail.com', 392009652, 12, 'right text', 'anzor', '???', 13, 14, 15),
  (3, '1234', '246742188', 'bb@gmail.com', 368497600, 17, 'left text', 'ilya', 'zemlya', 18, 19, 20),

INSERT INTO
  `messages` (`sender_id`, `receiver_id`, `message`, `filepath`, `creation_date`, `viewed`)
VALUES
  (0, 1, 'this is testing', 21, 22, 0),
  (2, 3, 'this is fake', 23, 24, 0),
  (1, 2, 'fakefactorio', 25, 26, 0),
  (2, 3, 'lie', 27, 28, 1),

INSERT INTO
  `tg_notifications ` (`notification_id`, `tg_id`, `message`, `executed`, `execution_date`, `creation_date`)
VALUES
  (0, 'kekmarakek', 'this is testing', 0, 29, 30),
  (1, 'kekmarakek', 'this is fake', 0, 31, 32),
  (2, 'kekmarakek', 'fakefactorio', 1, 33, 34),
  (3, 'kekmarakek', 'lie',1, 35, 36),

