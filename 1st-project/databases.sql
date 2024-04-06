CREATE DATABASE IF NOT EXISTS fst_app;
use fst_app;

CREATE TABLE users(
    id          int(255) auto_increment not null,
    name        varchar(100), 
    surname     varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    dates       date not null,
    CONSTRAINT  pk_users PRIMARY KEY(id),
    CONSTRAINT  Uq_email UNIQUE(email)
)ENGINE=InnoDb;


CREATE TABLE notes (
    id          int(255) auto_increment not null,
    user_id     int(250) not null,
    title       varchar(255) not null,
    description MEDIUMTEXT,
    dates       date not null,
    CONSTRAINT  pk_notes PRIMARY KEY(id),
    CONSTRAINT  fk_note_user FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDb;