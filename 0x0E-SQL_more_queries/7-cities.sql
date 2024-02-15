-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database to work with it
USE hbtn_0d_usa;
-- creates table in the database states
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
