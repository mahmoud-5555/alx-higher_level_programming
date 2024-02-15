--this code should list privileges of the MySQL
--users user_0d_1 and user_0d_2 on your server (in localhost).
-- Grant privileges to existing users only
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER ON *.* TO 'user_0d_1'@'localhost';

-- Check if 'user_0d_2' exists before granting privileges
SELECT COUNT(*) INTO @user_0d_2_exists FROM mysql.user WHERE User = 'user_0d_2' AND Host = 'localhost';

-- Grant privileges to 'user_0d_2' if it exists
IF @user_0d_2_exists > 0 THEN
    GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER ON *.* TO 'user_0d_2'@'localhost';
END IF;
