CREATE DATABASE common;
USE common;

CREATE TABLE users (
    user_id int PRIMARY KEY AUTO_INCREMENT,
    password_hash text,
    phone varchar(255),
    email varchar(255),
    tg_id int DEFAULT 0,
    tg_authdate int,
    tg_hash text,
    first_name varchar(255),
    last_name varchar(255),
    last_auth int,
    last_update int,
    registration_date int
);

CREATE TABLE messages (
    message_id int PRIMARY KEY AUTO_INCREMENT,
    sender_id int,
    receiver_id int,
    message text,
    filepath text,
    creation_date int,
    viewed bool
);

CREATE TABLE tg_notifications (
    notification_id int PRIMARY KEY AUTO_INCREMENT,
    tg_id int,
    message text,
    executed bool,
    execution_date int,
    creation_date int
);

INSERT INTO
  users (`password_hash`, `phone`, `email`, `tg_id`, `tg_authdate`, `tg_hash`, `first_name`, `last_name`, `last_auth`, `last_update`, `registration_date`)
VALUES
  ('1234', '891045245', 'qq@gmail.com', 122031432, 2, 'some text', 'oleg', 'grinya', 3, 4, 5),
  ('1234', '891045535', 'ww@gmail.com', 297002761, 7, 'another text', 'kolyan', 'shkalka', 8, 9, 10),
  ('1234', '812045245', 'nn@gmail.com', 392009652, 12, 'right text', 'anzor', '???', 13, 14, 15),
  ('1234', '246742188', 'bb@gmail.com', 368497600, 17, 'left text', 'ilya', 'zemlya', 18, 19, 20);

INSERT INTO
  messages (`sender_id`, `receiver_id`, `message`, `filepath`, `creation_date`, `viewed`)
VALUES
  (0, 1, 'this is testing', 'test.txt', 22, 0),
  (2, 3, 'this is fake', 'test.txt', 24, 0),
  (1, 2, 'fakefactorio', 'test.txt', 26, 0),
  (2, 3, 'lie', 'test.txt', 28, 1);

INSERT INTO
  tg_notifications (`tg_id`, `message`, `executed`, `execution_date`, `creation_date`)
VALUES
  (122031432, 'this is testing 1', 1, 29, 30),
  (122031432, 'this is testing 2', 0, 29, 30),
  (122031432, 'this is testing 3', 0, 29, 30),
  (297002761, 'this is fake OOOOOOO', 0, 31, 32),
  (392009652, 'fakefactorio !123123124', 1, 33, 34),
  (368497600, 'lie',1, 35, 36);
