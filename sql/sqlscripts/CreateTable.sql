CREATE TABLE Admin (
id INT(2) NOT NULL AUTO_INCREMENT,
username VARCHAR(10) NOT NULL,
password VARCHAR(30) NOT NULL,
CONSTRAINT id_pk PRIMARY KEY (id)
);

CREATE TABLE Continant (
continantID VARCHAR(5) NOT NULL,
continantName VARCHAR(30) NOT NULL UNIQUE,
CONSTRAINT continantID_pk PRIMARY KEY (continantID)
);

CREATE TABLE Country
(
	countryID VARCHAR(5) NOT NULL,
	countryName VARCHAR(50) NOT NULL UNIQUE,
	capital VARCHAR(50) NOT NULL,
	continant_ID VARCHAR(5) NOT NULL,
	CONSTRAINT countryID_pk PRIMARY KEY(countryID),
	CONSTRAINT continant_ID_fk FOREIGN KEY (continant_ID) references continant(continantID)
);
