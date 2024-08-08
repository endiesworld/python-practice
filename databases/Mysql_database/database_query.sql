CREATE DATABASE projects;
use projects;
CREATE TABLE projects(project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id));

CREATE TABLE tasks( task_id INT NOT NULL AUTO_INCREMENT, project_id INT NOT NULL, description VARCHAR(255), PRIMARY KEY(task_id), FOREIGN KEY(project_id) REFERENCES projects(project_id));

show tables;

INSERT INTO projects(title, description) VALUES ("Organize Photos", "Organize old iphone photos by year");

INSERT INTO tasks(project_id, description) VALUES(1, "Organise 2020 photos");

INSERT INTO tasks(project_id, description) VALUES(1, "Organise 2019 photos");

INSERT INTO projects(title, description) VALUES ("Read More", "Read a book a month this year");

INSERT INTO tasks(project_id, description) VALUES(2, "Read The Huntress");

