DROP DATABASE IF EXISTS navicourse CASCADE;

CREATE DATABASE navicourse;

CREATE TABLE navicourse.ratings (
    user_id UUID PRIMARY KEY,
    course_id INT8,
    rating FLOAT8
)

IMPORT TABLE navicourse.courses (
    course_id UUID PRIMARY KEY,
    title STRING,
    description STRING,
    rating INT8,
    link STRING,
    source STRING
) 
CSV DATA ('<Insert Link Here>.csv');