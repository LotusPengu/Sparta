CREATE TABLE personnel (
	first_name VARCHAR (20),
	last_name VARCHAR (20),
	notes VARCHAR (max),
	phone_number CHAR (11),
	birthdate DATE,
	first_shift_start DATETIME,
	lunch_breaks TIME, number_of_awards INT,
	hourly_rate DECIMAL (4,2), -- (precision, scale) e.g., 4 digits, 2 after the decimal point
	height_metres FLOAT (24), -- (maximum digits)
	is_full_time BIT -- 1 or zero, true or false 
);