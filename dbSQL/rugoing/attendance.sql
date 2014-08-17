USE rugoing;

CREATE TABLE `attendance` (
  `userid` int(11) NOT NULL DEFAULT '0',
  `eventid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`userid`,`eventid`),
  KEY `attendance_ibfk_2` (`eventid`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`eventid`) REFERENCES `events` (`eventid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


