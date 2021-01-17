DROP DATABASE IF EXISTS navicourse CASCADE;

CREATE DATABASE navicourse;

CREATE TABLE navicourse.ratings (
    user_id UUID PRIMARY KEY,
    course_id INT8,
    rating FLOAT8
);

CREATE TABLE navicourse.courses (
    id INT8 PRIMARY KEY,
    title STRING,
    description STRING,
    rating STRING,
    link STRING,
    source STRING
);

\| cat Udacity.sql
