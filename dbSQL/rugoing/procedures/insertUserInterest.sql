DROP PROCEDURE IF EXISTS rugoing.insertUserInterest;
CREATE PROCEDURE rugoing.`insertUserInterest`(IN userin VARCHAR(255),IN interest VARCHAR(255))
BEGIN
 DECLARE userid INT(11);
 DECLARE interestid INT(11);
 DECLARE checker INT(11);
 SELECT count(*) INTO userid FROM users WHERE users.username=userin;
 SELECT count(*) INTO interestid FROM tags WHERE tags.name=interest;
 IF( userid > 0)
 THEN
  IF(interestid >0)
  THEN
    SELECT users.id INTO userid FROM users WHERE users.username=userin;
    SELECT tags.tagid INTO interestid FROM tags WHERE tags.name=interest;
    SELECT COUNT(*) INTO checker FROM userinterest WHERE userinterest.tagid=interestid AND userinterest.userid=userid;
    IF(checker = 0)
    THEN
      INSERT INTO userinterest (userinterest.userid,userinterest.tagid) VALUES(userid, interestid);
    END IF;
  ELSE
    INSERT INTO tags(tags.name) VALUES (interest);
    SELECT users.id INTO userid FROM users WHERE users.username=userin;
    SELECT tags.tagid INTO interestid FROM tags WHERE tags.name=interest;
    INSERT INTO userinterest (userinterest.userid,userinterest.tagid) VALUES(userid, interestid);
  END IF;
 END IF;

END;
