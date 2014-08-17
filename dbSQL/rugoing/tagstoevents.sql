USE rugoing;

CREATE TABLE `tagstoevents` (
  `eventid` int(11) NOT NULL DEFAULT '0',
  `tagid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`eventid`,`tagid`),
  KEY `tagstoevents_ibfk_2` (`tagid`),
  CONSTRAINT `tagstoevents_ibfk_1` FOREIGN KEY (`eventid`) REFERENCES `events` (`eventid`),
  CONSTRAINT `tagstoevents_ibfk_2` FOREIGN KEY (`tagid`) REFERENCES `tags` (`tagid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


insert into rugoing.tagstoevents(eventid,tagid) values (1,1);
insert into rugoing.tagstoevents(eventid,tagid) values (6,1);
insert into rugoing.tagstoevents(eventid,tagid) values (6,2);
insert into rugoing.tagstoevents(eventid,tagid) values (7,3);
insert into rugoing.tagstoevents(eventid,tagid) values (3,4);
insert into rugoing.tagstoevents(eventid,tagid) values (8,10);
