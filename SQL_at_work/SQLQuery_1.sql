-- DROP TABLE IF EXISTS genre

CREATE TABLE genre (
    type_id INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
    film_type VARCHAR (50)
);

INSERT INTO genre (
    film_type
)
VALUES
    ('Sci-fi'),
    ('Action'),
    ('Drama');

DROP TABLE IF EXISTS languages

CREATE TABLE languages (
    language_id INT PRIMARY KEY IDENTITY (1,1),
    film_language VARCHAR (20)
);

INSERT INTO languages (
    film_language
)
VALUES 
    ('English'),
    ('French');

DROP TABLE IF  EXISTS film_table

CREATE TABLE film_table (
    film_id  INT PRIMARY KEY IDENTITY (1,1) NOT NULL,
    film_name VARCHAR (100),
    film_type INT FOREIGN KEY REFERENCES genre,
    date_of_release DATE,
    director VARCHAR (20),
    writer VARCHAR (100),
    star VARCHAR (100),
    film_language INT FOREIGN KEY REFERENCES languages,
    official_website VARCHAR (100),
    plot_summary VARCHAR (1000),
    runtime_mins INT
);

INSERT INTO film_table (
    film_name, film_type, date_of_release, director, writer, star,
    film_language, official_website, plot_summary, runtime_mins
)
VALUES (
    'Inception', 1, '2010-07-16', 'Christopher Nolan', 'Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page',
     1, 'https://www.warnerbros.com/movies/inception', 'A thief enters the dreams of others to steal their deepest secrets but is tasked with planting an idea into someones mind.',
     148
), (
    'The Shawshank Redemption', 3, '1994-09-23', 'Frank Darabont', 'Stephen King, Frank Darabont', 'Tim Robbins, Morgan Freeman', 1,
    'https://www.warnerbros.com/movies/shawshank-redemption', 'A man is sentenced to life in Shawshank State Penitentiary for a crime he didnt commit and befriends a fellow inmate.',
    142
);
