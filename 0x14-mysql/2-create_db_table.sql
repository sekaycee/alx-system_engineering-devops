-- Create a database named tyrell_corp
-- +Create a table named nexus6 and add at least one entry to it
CREATE DATABASE IF NOT EXISTS tyrell_corp;
   USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL
       );
INSERT INTO nexus6 (name) VALUES ('Marvy');
INSERT INTO nexus6 (name) VALUES ('Caleb');
INSERT INTO nexus6 (name) VALUES ('Chioma');
 GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
 FLUSH PRIVILEGES;
