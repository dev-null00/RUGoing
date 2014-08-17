import unittest
import insertRUEvent

#InsertEvent 2 test cases

#1. Test case for boundary testing of insertEvent
#Boundary value:
#The "eventtime" filed of inserted event should be equal to or larger than BoundaryDate=currentDate.
#
#We use 3 input data:
#(1) "eventtime" of event < BoundaryDate;
#(2) "eventtime" of event = BoundaryDate;
#(3) "eventtime" of event > BoundaryDate;
class InsertEventBoundaryTestCase(unittest.TestCase):
	def setUp(self):
		pass
		#keep name as valid input!
		self.name = "Rutgers Football Game1"
		self.location = "busch campus"
		self.url = "www.rutgers.edu"
		self.synopsis = "great event!"
		self.category = "other"
		self.target_audience = "students"
		
	def tearDown(self):
		pass
		
	def testToday(self):
		str_format = "%b %d %Y %H:%M:%S"
		today = datetime.now()
		today_str = today.strftime(str_format)
		return insertRUEvent.insertEvent(self.name,self.location,self.url,self.synopsis,
									self.category,self.target_audience,today_str)
	
	def testYesterday(self):
		str_format = "%b %d %Y %H:%M:%S"
		one_day = timedelta(days=1)
		today = datetime.now()
		yesterday = today - one_day
		yesterday_str = yesterday.strftime(str_format)
		return insertRUEvent.insertEvent(self.name,self.location,self.url,self.synopsis,
									self.category,self.target_audience,yesterday_str)
	
	def testTomorrow(self):
		str_format = "%b %d %Y %H:%M:%S"
		one_day = timedelta(days=1)
		today = datetime.now()
		tomorrow = today + one_day
		tomorrow_str = tomorrow.strftime(str_format)
		return insertRUEvent.insertEvent(self.name,self.location,self.url,self.synopsis,
									self.category,self.target_audience,tomorrow_str)	
	def runTest(self):
		result = testToday()
		assert result == true, 'error occured for testToday'
		result = testYesterday()
		assert result == false, 'error occured for testYesterday'
		result = testTomorrow()
		assert result == true, 'error occured for testTomorrow'

#2. Test case for equivalence testing of insertEvent
# The "name" field of the event should be a string with NUM=number of characters in "name" and 6<=NUM<=60 
# The input date can be divided into 3 partitions.
# (1) NUM < 6;
# (2) 6<= NUM <= 60
# (3) NUM > 60
class InsertEventEquivalenceTestCase(unittest.TestCase):
	def setUp(self):
		pass
		str_format = "%b %d %Y %H:%M:%S"
		today = datetime.now()
		today_str = today.strftime(str_format)
		#keep eventtime as valid input!
		self.eventtime = today_str
		self.location = "busch campus"
		self.url = "www.rutgers.edu"
		self.synopsis = "great event!"
		self.category = "other"
		self.target_audience = "students"
		
	def tearDown(self):
		pass
		
	def testPartition1(self):
		self.name = "game1"
		return insertRUEvent.insertEvent(self.name,self.location,self.url,self.synopsis,
									self.category,self.target_audience,today_str)
	
	def testPartition2(self):
		self.name = "ECE Annual Faculty Meeting"
		return insertRUEvent.insertEvent(self.name,self.location,self.url,self.synopsis,
									self.category,self.target_audience,yesterday_str)
	
	def testPartition3(self):
		self.name = "virus!virus!virus!virus!virus!virus!virus!virus!virus!virus!virus!virus!"
		return insertRUEvent.insertEvent(self.name,self.location,self.url,self.synopsis,
									self.category,self.target_audience,tomorrow_str)	
	def runTest(self):
		result = testPartition1()
		assert result == false, 'error occured for testPartition1'
		result = testPartition2()
		assert result == true, 'error occured for testPartition2'
		result = testPartition3()
		assert result == false, 'error occured for testPartition3'