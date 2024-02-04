-- SQLite

CREATE TABLE UserData (
	email data_type PRIMARY KEY,
   	first_name data_type NOT NULL,
    last_name data_type NOT NULL,
	password data_type NOT NULL,
	table_constraints
) ;
-- ​
INSERT INTO UserData 
(email,first_name, last_name,password) 
VALUES ("pc@gmail.com", "prashant","choubey","abc");

 ​
SELECT * FROM UserData;