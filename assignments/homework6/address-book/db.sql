# create db
CREATE DATABASE addressDb;
USE addressDb;

# create table
CREATE TABLE Addresses(
	Id INT PRIMARY KEY AUTO_INCREMENT,
	Full_Name VARCHAR(30),
	Full_Address VARCHAR(30),
	City_Name VARCHAR(30),
	State_Name VARCHAR(2),
	Zip_Code INT
);

# query table
USE addressDb;
INSERT INTO Addresses(Full_Name, Full_Address, City_Name, State_Name, 	Zip_Code)
VALUES('Lisa Leslie', '2939 38th Street', 'Seattle', 'WA', 87933)