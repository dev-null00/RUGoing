USE rugoing;

CREATE TABLE `userinterest` (
  `userid` int(11) NOT NULL DEFAULT '0',
  `tagid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`userid`,`tagid`),
  UNIQUE KEY `uniqueinterest` (`userid`,`tagid`),
  KEY `userinterest_ibfk_2` (`tagid`),
  CONSTRAINT `userinterest_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`id`),
  CONSTRAINT `userinterest_ibfk_2` FOREIGN KEY (`tagid`) REFERENCES `tags` (`tagid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


insert into rugoing.userinterest(userid,tagid) values (1,1);
insert into rugoing.userinterest(userid,tagid) values (3,1);
insert into rugoing.userinterest(userid,tagid) values (4,1);
insert into rugoing.userinterest(userid,tagid) values (60,1);
insert into rugoing.userinterest(userid,tagid) values (62,1);
insert into rugoing.userinterest(userid,tagid) values (66,1);
insert into rugoing.userinterest(userid,tagid) values (68,1);
insert into rugoing.userinterest(userid,tagid) values (69,1);
insert into rugoing.userinterest(userid,tagid) values (70,1);
insert into rugoing.userinterest(userid,tagid) values (74,1);
insert into rugoing.userinterest(userid,tagid) values (75,1);
insert into rugoing.userinterest(userid,tagid) values (80,1);
insert into rugoing.userinterest(userid,tagid) values (81,1);
insert into rugoing.userinterest(userid,tagid) values (89,1);
insert into rugoing.userinterest(userid,tagid) values (91,1);
insert into rugoing.userinterest(userid,tagid) values (1,2);
insert into rugoing.userinterest(userid,tagid) values (81,2);
insert into rugoing.userinterest(userid,tagid) values (1,3);
insert into rugoing.userinterest(userid,tagid) values (5,3);
insert into rugoing.userinterest(userid,tagid) values (62,3);
insert into rugoing.userinterest(userid,tagid) values (66,3);
insert into rugoing.userinterest(userid,tagid) values (68,3);
insert into rugoing.userinterest(userid,tagid) values (69,3);
insert into rugoing.userinterest(userid,tagid) values (70,3);
insert into rugoing.userinterest(userid,tagid) values (74,3);
insert into rugoing.userinterest(userid,tagid) values (80,3);
insert into rugoing.userinterest(userid,tagid) values (81,3);
insert into rugoing.userinterest(userid,tagid) values (88,3);
insert into rugoing.userinterest(userid,tagid) values (89,3);
insert into rugoing.userinterest(userid,tagid) values (91,3);
insert into rugoing.userinterest(userid,tagid) values (1,4);
insert into rugoing.userinterest(userid,tagid) values (3,4);
insert into rugoing.userinterest(userid,tagid) values (24,4);
insert into rugoing.userinterest(userid,tagid) values (60,4);
insert into rugoing.userinterest(userid,tagid) values (62,4);
insert into rugoing.userinterest(userid,tagid) values (66,4);
insert into rugoing.userinterest(userid,tagid) values (68,4);
insert into rugoing.userinterest(userid,tagid) values (69,4);
insert into rugoing.userinterest(userid,tagid) values (70,4);
insert into rugoing.userinterest(userid,tagid) values (74,4);
insert into rugoing.userinterest(userid,tagid) values (75,4);
insert into rugoing.userinterest(userid,tagid) values (80,4);
insert into rugoing.userinterest(userid,tagid) values (81,4);
insert into rugoing.userinterest(userid,tagid) values (85,4);
insert into rugoing.userinterest(userid,tagid) values (86,4);
insert into rugoing.userinterest(userid,tagid) values (87,4);
insert into rugoing.userinterest(userid,tagid) values (88,4);
insert into rugoing.userinterest(userid,tagid) values (89,4);
insert into rugoing.userinterest(userid,tagid) values (91,4);
insert into rugoing.userinterest(userid,tagid) values (82,5);
insert into rugoing.userinterest(userid,tagid) values (24,6);
insert into rugoing.userinterest(userid,tagid) values (77,6);
insert into rugoing.userinterest(userid,tagid) values (3,7);
insert into rugoing.userinterest(userid,tagid) values (24,7);
insert into rugoing.userinterest(userid,tagid) values (60,7);
insert into rugoing.userinterest(userid,tagid) values (1,8);
insert into rugoing.userinterest(userid,tagid) values (24,8);
insert into rugoing.userinterest(userid,tagid) values (38,8);
insert into rugoing.userinterest(userid,tagid) values (1,9);
insert into rugoing.userinterest(userid,tagid) values (84,10);
insert into rugoing.userinterest(userid,tagid) values (88,12);
insert into rugoing.userinterest(userid,tagid) values (89,13);
insert into rugoing.userinterest(userid,tagid) values (91,13);
insert into rugoing.userinterest(userid,tagid) values (89,14);
insert into rugoing.userinterest(userid,tagid) values (91,14);
insert into rugoing.userinterest(userid,tagid) values (89,15);
insert into rugoing.userinterest(userid,tagid) values (91,15);
insert into rugoing.userinterest(userid,tagid) values (3,16);
insert into rugoing.userinterest(userid,tagid) values (60,16);
insert into rugoing.userinterest(userid,tagid) values (92,17);
insert into rugoing.userinterest(userid,tagid) values (102,18);
