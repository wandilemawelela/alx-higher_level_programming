-- Creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on MySQL server.

-- If the database doesn't exist, create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the states table if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
