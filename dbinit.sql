DROP DATABASE IF EXISTS navicourse CASCADE;

CREATE DATABASE navicourse;

CREATE TABLE navicourse.ratings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INT8,
    course_id INT8,
    rating FLOAT8
);

CREATE TABLE navicourse.courses_in_progress (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INT8,
    course_id INT8
);

CREATE TABLE navicourse.users (
    user_id INT8 PRIMARY KEY,
    name STRING
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
\| cat Harvard.sql
