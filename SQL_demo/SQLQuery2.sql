INSERT INTO personnel (
	first_name, last_name, notes, phone_number, 
	birthdate, first_shift_start, lunch_breaks, number_of_awards,
	hourly_rate, height_metres, is_full_time
) VALUES (
	'Toby', -- VARCHAR
	'Gjerstrup', -- VARCHAR
	'The coolest person known to man', -- VARCHAR
	'07473871407', -- CHAR
	'2001-03-06', -- DATE
	'2023-11-19 11:13:00', -- DATETIME
	'13:00:00', -- DATE
	4, -- INT
	12.75, -- DECIMAL
	1.77e1, -- FLOAT
	1 -- BIT
);
