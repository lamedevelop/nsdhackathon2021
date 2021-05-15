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
