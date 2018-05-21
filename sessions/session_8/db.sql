# create db
CREATE DATABASE employeeDb;
USE employeeDb;

# create table
CREATE TABLE Employees(
	Id INT PRIMARY KEY auto_increment,
	First_Name VARCHAR(30),
	Last_Name VARCHAR(30),
	Age INT,
	Gender CHAR(1),
	Income FLOAT
)

# query table
USE employeeDb;
INSERT INTO Employees (First_Name, Last_Name, Age, Gender, Income)
VALUES('Kal', 'Vis', 20, 'F', 100.01)

SELECT * FROM Employees