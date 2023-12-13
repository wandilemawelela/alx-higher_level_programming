-- Creates the table force_name on your MySQL server.

USE hbtn_0d_2;

-- Check if the table force_name already exists
SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'force_name';

-- If the table doesn't exist, create it
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
