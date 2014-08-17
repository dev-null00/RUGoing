USE rugoing;

CREATE TABLE `comments` (
  `comment` varchar(250) NOT NULL,
  `commentid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL DEFAULT '0',
  `eventid` int(11) NOT NULL DEFAULT '0',
  `entrytime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`commentid`),
  UNIQUE KEY `userid` (`userid`,`eventid`),
  KEY `comments_ibfk_2` (`eventid`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`eventid`) REFERENCES `events` (`eventid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;


insert into rugoing.comments(comment,commentid,userid,eventid,entrytime) values ('hello there',1,85,1,'2010-11-06 22:50:41');
