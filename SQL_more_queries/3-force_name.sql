-- Creates a table force_name that cannot have a null name parameter
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL
);
