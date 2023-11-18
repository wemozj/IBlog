DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id integer primary key AUTOINCREMENT,
    title varchar(255) NOT NULL,
    content TEXT NOT NULL,
    created_time TIMESTAMP NOT NULL default CURRENT_TIMESTAMP,
    updated_time TIMESTAMP NOT NULL default CURRENT_TIMESTAMP
);