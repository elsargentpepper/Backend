CREATE TABLE technologies(
    technologies_id SERIAL PRIMARY KEY,
    name varchar(100));

CREATE TABLE levels(
    levels_id SERIAL PRIMARY KEY,
    name varchar(50));

CREATE TABLE questions(
    questions_id SERIAL PRIMARY KEY,
    answers text[],
    image varchar(200),
    level integer references levels(levels_id),
    technology integer references technologies(technologies_id),
    question text);   

CREATE TABLE users(
    users_id SERIAL PRIMARY KEY,
    name varchar(100),
    email varchar(100),
    password varchar(20),
    login_type varchar(20),
    badges text[],
    prefered_technologies text[]);

CREATE TABLE progress(
    progress_id SERIAL PRIMARY KEY,
    percentage integer,
    user_id integer references users(users_id),
    technology integer references technologies(technologies_id)); 