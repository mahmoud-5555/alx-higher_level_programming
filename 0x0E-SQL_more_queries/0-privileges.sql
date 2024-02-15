--this code should list privileges of the MySQL
--users user_0d_1 and user_0d_2 on your server (in localhost).
SELECT * FROM INFORMATION_SCHEMA.USER_PRIVILEGES WHERE GRANTEE IN ('user_0d_1@localhost', 'user_0d_2@localhost');
