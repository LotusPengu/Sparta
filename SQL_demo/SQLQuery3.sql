DROP TABLE IF EXISTS films;

CREATE TABLE films (
	film_title VARCHAR (180) NOT NULL,
	release_date DATE,
	box_office_USD DECIMAL (10, 0),
	runtime_mins INT,
	oscar_winning BIT DEFAULT 0
);

INSERT INTO films (
	film_title, release_date, box_office_USD, runtime_mins, oscar_winning
) VALUES (
	'Shrek',
	'2001-06-29',
	484000000,
	95,
	1
),(
	'Shrek 2',
	'2004-07-2',
	9198000000,
	105,
	0
),(
	'Shrek The Third',
	'2007-05-06',
	8134000000,
	93,
	0
);