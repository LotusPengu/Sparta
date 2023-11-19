DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
	course_id INT PRIMARY KEY IDENTITY (1,1), -- SQL will terminate anything that violates the PK constraint
	-- key identity means the PK will start at the first value and increment by the second
	course_name VARCHAR (20) UNIQUE -- Value must be unique to eachother or SQL rejects it 
);

INSERT INTO courses (
	course_name
) VALUES
	('C# Development'),
	('Java Development'),
	('Business Analyst'),
	('Data Engineer');

DROP TABLE IF EXISTS students;
CREATE TABLE students (
	student_id INT PRIMARY KEY IDENTITY (1,1),
	student_name VARCHAR (20),
	course_id INT FOREIGN KEY REFERENCES courses (course_id) -- foreign key, course_id is also included in courses table
);

INSERT INTO students
	(student_name, course_id)
VALUES
	('Alice', 1),
	('Bob', 1),
	('Charlie', 2);