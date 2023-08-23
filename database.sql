CREATE TABLE Ages (
name VARCHAR(128),
age INT
);


DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Eonan', 40);
INSERT INTO Ages (name, age) VALUES ('Rubhan', 17);
INSERT INTO Ages (name, age) VALUES ('Sakina', 30);
INSERT INTO Ages (name, age) VALUES ('Charlee', 37);
INSERT INTO Ages (name, age) VALUES ('Akam', 28);


SELECT hex(name || age) AS X FROM Ages ORDER BY X