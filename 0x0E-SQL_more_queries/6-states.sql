-- script that creates the table id_not_null on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL);
