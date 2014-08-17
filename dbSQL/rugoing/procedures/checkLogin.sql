DROP PROCEDURE IF EXISTS rugoing.checkLogin;
CREATE PROCEDURE rugoing.`checkLogin`(IN username VARCHAR(255), IN userpassword VARCHAR(255))
BEGIN
SELECT COUNT(*) AS RESULT FROM users u where u.username= username AND u.belly= userpassword;
END;