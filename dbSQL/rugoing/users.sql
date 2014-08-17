USE rugoing;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `belly` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;


insert into rugoing.users(id,username,belly,fname,lname) values (1,'helloer','hello','helloer','helloer');
insert into rugoing.users(id,username,belly,fname,lname) values (3,'tester2','h','h','h');
insert into rugoing.users(id,username,belly,fname,lname) values (4,'help','help','help','help');
insert into rugoing.users(id,username,belly,fname,lname) values (5,'jayu','jayp','jayf','jayl');
insert into rugoing.users(id,username,belly,fname,lname) values (7,'samu','samp','samf','saml');
insert into rugoing.users(id,username,belly,fname,lname) values (8,'string','string','string','string');
insert into rugoing.users(id,username,belly,fname,lname) values (12,'blahu','blahp','blahf','blahl');
insert into rugoing.users(id,username,belly,fname,lname) values (23,'paul','','','');
insert into rugoing.users(id,username,belly,fname,lname) values (24,'a','a','a','a');
insert into rugoing.users(id,username,belly,fname,lname) values (26,'b','b','b','b');
insert into rugoing.users(id,username,belly,fname,lname) values (27,'c','c','c','c');
insert into rugoing.users(id,username,belly,fname,lname) values (29,'d','d','d','d');
insert into rugoing.users(id,username,belly,fname,lname) values (37,'e','a','e','e');
insert into rugoing.users(id,username,belly,fname,lname) values (38,'x','x','x','x');
insert into rugoing.users(id,username,belly,fname,lname) values (40,'solomon','1234','solomon','lasluisa');
insert into rugoing.users(id,username,belly,fname,lname) values (48,'o','o','o','o');
insert into rugoing.users(id,username,belly,fname,lname) values (50,'w','w','w','w');
insert into rugoing.users(id,username,belly,fname,lname) values (60,'h','h','h','h');
insert into rugoing.users(id,username,belly,fname,lname) values (62,'blah','blah','blah','blah');
insert into rugoing.users(id,username,belly,fname,lname) values (66,'solo','solo','solo','solo');
insert into rugoing.users(id,username,belly,fname,lname) values (68,'j','newPassword','firstName','lastname');
insert into rugoing.users(id,username,belly,fname,lname) values (69,'q','q','q','q');
insert into rugoing.users(id,username,belly,fname,lname) values (70,'u','u','u','u');
insert into rugoing.users(id,username,belly,fname,lname) values (74,'p','p','p','p');
insert into rugoing.users(id,username,belly,fname,lname) values (75,'newuser','newuser','newuser','newuser');
insert into rugoing.users(id,username,belly,fname,lname) values (77,'ab','ab','ab','ab');
insert into rugoing.users(id,username,belly,fname,lname) values (79,'abc','abc','abc','abc');
insert into rugoing.users(id,username,belly,fname,lname) values (80,'abcd','abcd','abcd','acbd');
insert into rugoing.users(id,username,belly,fname,lname) values (81,'aa','aa','aa','aa');
insert into rugoing.users(id,username,belly,fname,lname) values (82,'zxc','zxc','zxc','zxc');
insert into rugoing.users(id,username,belly,fname,lname) values (83,'asd','asd','asd','asd');
insert into rugoing.users(id,username,belly,fname,lname) values (84,'asda','asda','asda','asda');
insert into rugoing.users(id,username,belly,fname,lname) values (85,'nanoer','','','');
insert into rugoing.users(id,username,belly,fname,lname) values (86,'nanoed','nanoed','nanoed','nanoed');
insert into rugoing.users(id,username,belly,fname,lname) values (87,'nanoer2','nanoer2','fname','lname');
insert into rugoing.users(id,username,belly,fname,lname) values (88,'test2','test2','test2','test2');
insert into rugoing.users(id,username,belly,fname,lname) values (89,'whocares','whocares','whocares','whocares');
insert into rugoing.users(id,username,belly,fname,lname) values (91,'whocares2','whocares','whocares2','whocares');
insert into rugoing.users(id,username,belly,fname,lname) values (92,'','sda','sda','sda');
insert into rugoing.users(id,username,belly,fname,lname) values (102,'snegala','rutgers123','sneha','gala');
