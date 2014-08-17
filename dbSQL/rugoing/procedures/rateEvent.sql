DROP PROCEDURE IF EXISTS rugoing.rateEvent;
CREATE PROCEDURE rugoing.`rateEvent`(IN userin VARCHAR(255), IN ratingin INT(11), IN eventidin INT(11))
BEGIN
 DECLARE useridvar INT(11);
 SELECT users.id INTO useridvar FROM users WHERE users.username=userin;
 insert into rating ( rating, userid, eventid) VALUES (
   ratingin -- rating
  ,useridvar -- userid
  ,eventidin -- eventid
 );
END;
