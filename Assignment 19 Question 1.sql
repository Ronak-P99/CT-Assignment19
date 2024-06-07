use e_commerce_db;

CREATE TABLE Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    trainer_id INT
);
CREATE TABLE WorkoutSessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    duration_minutes VARCHAR(50),
    calories_burned VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
    );
    SELECT * FROM Members;
	SELECT * FROM WorkoutSessions;