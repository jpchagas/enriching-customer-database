use rbsdb;

CREATE TABLE person(
	id_person INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	gender INT NOT NULL,
	photo VARCHAR(50) NOT NULL
)

CREATE TABLE address(
	id_address INT AUTO_INCREMENT PRIMARY KEY,
	person_id INT NOT NULL,
	street VARCHAR(50) NOT NULL,
	number VARCHAR(50) NOT NULL,
	city VARCHAR(50) NOT NULL,
	state VARCHAR(50) NOT NULL,
	FOREIGN KEY (person_id)
        REFERENCES person (id_person)
)

