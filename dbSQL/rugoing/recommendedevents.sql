USE rugoing;

CREATE TABLE `recommendedevents` (
  `eventid` int(11) NOT NULL DEFAULT '0',
  `userid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`eventid`,`userid`),
  KEY `userid` (`userid`),
  CONSTRAINT `recommendedevents_ibfk_1` FOREIGN KEY (`eventid`) REFERENCES `events` (`eventid`),
  CONSTRAINT `recommendedevents_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


