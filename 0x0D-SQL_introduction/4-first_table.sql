-- creates a table called first_table in the current database
DROP TABLE IF EXISTS first_table;
CREATE TABLE first_table (
	`id` int DEFAULT NULL,
	`name` varchar(256)
)
