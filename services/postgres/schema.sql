\set ON_ERROR_STOP on

BEGIN;

--

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);


CREATE TABLE urls (
    id_urls BIGSERIAL PRIMARY KEY,
    url TEXT UNIQUE
);


CREATE TABLE messages (
    id BIGSERIAL PRIMARY KEY,
    creator_id INTEGER NOT NULL REFERENCES users(id),
    message TEXT NOT NULL,
    time TIMESTAMP NOT NULL DEFAULT current_timestamp

);

CREATE INDEX m3 ON messages(time, id, creator_id, message);
CREATE EXTENSION IF NOT EXISTS RUM;
CREATE INDEX search_query ON messages USING RUM(to_tsvector('english', message));

commit; 
