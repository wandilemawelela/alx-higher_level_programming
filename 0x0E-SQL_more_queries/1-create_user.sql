-- Creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges on MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, script should not fail

-- Check if the user already exists
SELECT * FROM mysql.user WHERE user = 'user_0d_1';

-- If the user doesn't exist, create it
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
