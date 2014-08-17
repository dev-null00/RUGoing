USE rugoing;

CREATE TABLE `rating` (
  `rating` int(11) DEFAULT NULL,
  `userid` int(11) NOT NULL DEFAULT '0',
  `eventid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`userid`,`eventid`),
  KEY `rating_ibfk_2` (`eventid`),
  CONSTRAINT `rating_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `rating_ibfk_2` FOREIGN KEY (`eventid`) REFERENCES `events` (`eventid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


insert into rugoing.rating(rating,userid,eventid) values (2,3,1);
insert into rugoing.rating(rating,userid,eventid) values (1,3,4);
insert into rugoing.rating(rating,userid,eventid) values (0,102,1);
