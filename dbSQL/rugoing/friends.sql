USE rugoing;

CREATE TABLE `friends` (
  `userid` int(11) NOT NULL DEFAULT '0',
  `friendsid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`userid`,`friendsid`),
  KEY `friends_ibfk_2` (`friendsid`),
  CONSTRAINT `friends_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `friends_ibfk_2` FOREIGN KEY (`friendsid`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


