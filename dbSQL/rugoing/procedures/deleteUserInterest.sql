DROP PROCEDURE IF EXISTS rugoing.deleteUserInterest;
CREATE PROCEDURE rugoing.`deleteUserInterest`(IN userin VARCHAR(255))
BEGIN
 DECLARE userid INT(11);
 SELECT users.id INTO userid FROM users WHERE users.username=userin;

 DELETE FROM userinterest
WHERE userinterest.userid =userid;

END;
