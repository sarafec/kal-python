CREATE DATABASE addressdb;
USE addressdb;

# create table
CREATE TABLE Addresses(
	Id INT PRIMARY KEY AUTO_INCREMENT,
	Full_Name VARCHAR(30),
	Full_Address VARCHAR(30),
	City_Name VARCHAR(30),
	State_Name VARCHAR(2),
	Zip_Code INT
);
