DROP PROCEDURE IF EXISTS rugoing.modifyUser;
CREATE PROCEDURE rugoing.`modifyUser`(IN userin VARCHAR(255), IN firstName VARCHAR(255), IN lastname VARCHAR(255), IN newPassword VARCHAR(255))
BEGIN
update users SET
  belly = newPassword
  ,fname = firstName
  ,lname = lastName
WHERE username = userin;

END;
