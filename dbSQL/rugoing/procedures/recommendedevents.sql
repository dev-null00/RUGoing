DROP PROCEDURE IF EXISTS rugoing.recommendedevents;
CREATE PROCEDURE rugoing.`recommendedevents`(IN userin VARCHAR(255))
BEGIN
SELECT DISTINCT events.eventid, events.name, events.location, events.timeofevent as `time`
  FROM userinterest, users, tags, tagstoevents,events
 WHERE users.id = userinterest.userid
 AND userinterest.tagid = tags.tagid
 AND events.eventid = tagstoevents.eventid
 AND tagstoevents.tagid = tags.tagid
 AND users.username=userin;
END;
