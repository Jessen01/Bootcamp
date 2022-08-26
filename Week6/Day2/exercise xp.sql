
-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_Mauritius.1252'
--     LC_CTYPE = 'English_Mauritius.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;
	
	
	
-- CREATE TABLE items(
--  	  items_id SERIAL PRIMARY KEY,
-- 	  first_name VARCHAR (50) NOT NULL,
--       items_price SMALLINT
--  	 );
-- 	INSERT INTO items (type_name, items_price)
-- 	VALUES('Small Desk', 100),
-- 		('Large Desk', 300),
-- 		('Fan' , 80);

-- CREATE TABLE customers (
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(50) NOT NULL
-- );

-- INSERT INTO customers(first_name,last_name)
-- VALUES ( 'Greg',  'Jones'),
-- 		('Sandra','Jones'),
-- 		('Scott','Scott'),
-- 		('Trevor','Green'),
-- 		('Melanie','Johnson')
-- 		;


-- All items, ordered by price (lowest to highest)

SELECT * FROM items ORDER BY price ASC;
-- Items with a price above 80 (80 included), ordered by price (highest to lowest)

SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;
-- The first 3 customers in alphabetical order of the first name (A-Z)
--  exclude the primary key column from the results.

SELECT * FROM customers ORDER BY first_name ASC LIMIT  3 ;
-- All last names (no other columns!), in reverse alphabetical order (Z-A)

SELECT last_name FROM customers ORDER BY last_name DESC;
	