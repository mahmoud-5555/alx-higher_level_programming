-- create the datatabse
CREATE DATABASE IF NOT EXISTS hbtn_0d_2
-- create the user 
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- do the  privileges on user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
