DROP TABLE IF EXISTS games;
CREATE TABLE games (
	game_id INT PRIMARY KEY IDENTITY (1,1),
	game_name VARCHAR (20),
	release_date DATE
);

DROP TABLE IF EXISTS colours;
CREATE TABLE colours (
	colour_id INT PRIMARY KEY IDENTITY (1,1),
	colour VARCHAR (20)
);


DROP TABLE IF EXISTS characters;
CREATE TABLE characters (
	character_id INT PRIMARY KEY IDENTITY (1,1),
	character_name VARCHAR (20),
	date_created DATE,
	game_from INT FOREIGN KEY REFERENCES games (game_id),
	primary_colour INT FOREIGN KEY REFERENCES colours (colour_id),
	awards_won INT,
	protagonist BIT
);
