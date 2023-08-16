-- add user GRANT SELECT


CREATE USER 
		IF NOT EXISTS 'user_0d_1'@'localhost' 
		IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES 
	ON database_name.*
	TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
