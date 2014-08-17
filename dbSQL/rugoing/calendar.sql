USE rugoing;

CREATE TABLE `calendar` (
  `userid` int(11) NOT NULL,
  `eventid` int(11) NOT NULL,
  KEY `userid` (`userid`),
  KEY `eventid` (`eventid`),
  CONSTRAINT `calendar_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `calendar_ibfk_2` FOREIGN KEY (`eventid`) REFERENCES `events` (`eventid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


