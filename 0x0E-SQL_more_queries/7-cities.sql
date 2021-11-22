-- script that creates the table id_not_null on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL, state_id INT NOT NULL FOREIGN KEY REFERENCES state_id(id), name VARCHAR(256) NOT NULL);
