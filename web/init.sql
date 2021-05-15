CREATE TABLE users (
    user_id int,
    phone varchar(255),
    email varchar(255),
    tg_id int,
    tg_authdate int,
    tg_hash varchar(500),
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
    creation_date int
);

CREATE TABLE tg_notifications (
    notification_id int,
    tg_id int,
    message text,
    executed bool,
    execution_date int,
    creation_date int
);
