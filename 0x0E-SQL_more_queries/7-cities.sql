-- Creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on MySQL server.

-- If the database doesn't exist, create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the states table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
   	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
