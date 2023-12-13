-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- If the database hbtn_0d_2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail

-- Check if the database hbtn_0d_2 already exists
SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = 'hbtn_0d_2';

-- If the database doesn't exist, create it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user user_0d_2 already exists
SELECT * FROM mysql.user WHERE user = 'user_0d_2';

-- If the user doesn't exist, create it
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user only on the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
