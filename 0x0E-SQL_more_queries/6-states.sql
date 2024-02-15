-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database to work with it
USE hbtn_0d_usa;
-- creates table in the database states
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
