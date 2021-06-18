CREATE TABLE technologies(
    technologies_id SERIAL PRIMARY KEY,
    name varchar(100) UNIQUE);

CREATE TABLE levels(
    levels_id SERIAL PRIMARY KEY,
    name varchar(50) UNIQUE);

CREATE TABLE questions(
    questions_id SERIAL PRIMARY KEY,
    answers text[],
    image varchar(200),
    level integer references levels(levels_id),
    technology integer references technologies(technologies_id),
    question text UNIQUE);   

CREATE TABLE users(
    users_id SERIAL PRIMARY KEY,
    name varchar(100),
    email varchar(100) UNIQUE,
    username varchar(50) UNIQUE,
    password varchar(50),
    login_type varchar(20),
    badges text[],
    prefered_technologies text[]);

CREATE TABLE progress(
    progress_id SERIAL PRIMARY KEY,
    percentage integer,
    user_id integer references users(users_id),
    technology integer references technologies(technologies_id)); 


INSERT INTO questions(answers,image,level,technology,question) VALUES(
    ARRAY['undefined','B','True','A'],
    'https://imgur.com/a/qyvmmVo',
    7,
    1,
    'What will be the output of the following JavaScript code?'
);