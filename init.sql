CREATE DATABASE IF NOT EXISTS hogwarts;
USE hogwarts;
CREATE TABLE IF NOT EXISTS Characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255),
    gender VARCHAR(255),
    house VARCHAR(255),
    dateOfBirth VARCHAR(10),
    yearOfBirth INT,
    wizard BOOLEAN,
    ancestry VARCHAR(255),
    eyeColour VARCHAR(255),
    hairColour VARCHAR(255),
    patronus VARCHAR(255),
    hogwartsStudent BOOLEAN,
    hogwartsStaff BOOLEAN,
    actor VARCHAR(255),
    alive BOOLEAN,
    image VARCHAR(255)
);

ALTER TABLE Characters
MODIFY COLUMN id INT AUTO_INCREMENT;

CREATE TABLE IF NOT EXISTS Spells (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

ALTER TABLE Spells
DROP PRIMARY KEY,
MODIFY COLUMN id VARCHAR(255) AUTO_INCREMENT,
ADD PRIMARY KEY (id);