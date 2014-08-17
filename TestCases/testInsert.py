import unittest
import insertEvent
import datetime

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
                str_format = "%A, %B %d, %Y  %I:%M %p"
                today = datetime.datetime.now()
                seconds=datetime.timedelta(seconds=60)
                today=today+seconds
                today_str = today.strftime(str_format)
                result=insertEvent.insertEvent(self.name,self.location,self.url,self.synopsis,self.category,self.target_audience,today_str)
                assert result.find('true') > 0
        
        def testYesterday(self):
                str_format = "%A, %B %d, %Y  %I:%M %p"
                one_day = datetime.timedelta(days=1)
                today = datetime.datetime.now()
                yesterday = today - one_day
                yesterday_str = yesterday.strftime(str_format)
                result=insertEvent.insertEvent(self.name,self.location,self.url,self.synopsis,self.category,self.target_audience,yesterday_str)
                assert result.find('false') > 0

        def testTomorrow(self):
                str_format = "%A, %B %d, %Y  %I:%M %p"
                one_day = datetime.timedelta(days=1)
                today = datetime.datetime.now()
                tomorrow = today + one_day
                tomorrow_str = tomorrow.strftime(str_format)
                result=insertEvent.insertEvent(self.name,self.location,self.url,self.synopsis,self.category,self.target_audience,tomorrow_str)
                assert result.find('true') > 0

#        def runTest(self):
#                result = testToday()
#                print result
#                assert result.find('true') > 0
#                result = testYesterday()
#                assert result.find('true') > 0 
#                result = testTomorrow()
#                assert result.find('true') > 0

#2. Test case for equivalence testing of insertEvent
# The "name" field of the event should be a string with NUM=number of characters in "name" and 6<=NUM<=60 
# The input date can be divided into 3 partitions.
# (1) NUM < 6;
# (2) 6<= NUM <= 60
# (3) NUM > 60
class InsertEventEquivalenceTestCase(unittest.TestCase):
        def setUp(self):
                str_format = "%A, %B %d, %Y  %I:%M %p"
                today = datetime.datetime.now()
                seconds=datetime.timedelta(seconds=60)
                today=today+seconds
                self.today_str = today.strftime(str_format)
                #keep eventtime as valid input!
                #self.eventtime = today_str
                self.location = "busch campus"
                self.url = "www.rutgers.edu"
                self.synopsis = "great event!"
                self.category = "other"
                self.target_audience = "students"
                
        def testPartition1(self):
                self.name = "game1"
                result=insertEvent.insertEvent(self.name,self.location,self.url,self.synopsis,self.category,self.target_audience,self.today_str)
                assert result.find('false') > 0
        
        def testPartition2(self):
                self.name = "ECE Annual Faculty Meeting"
                result=insertEvent.insertEvent(self.name,self.location,self.url,self.synopsis,self.category,self.target_audience,self.today_str)
                assert result.find('true') > 0
        
        def testPartition3(self):
                self.name = "virus!virus!virus!virus!virus!virus!virus!virus!virus!virus!virus!virus!"
                result=insertEvent.insertEvent(self.name,self.location,self.url,self.synopsis,self.category,self.target_audience,self.today_str)        
                assert result.find('false') > 0
#        def runTest(self):
#                result=testPartition1()
#                print "wtf"
#                print result
#                assert result.find('false') > 0
#                result=testPartition2()
#                print result
#                assert result.find('false') > 0
#                result=testPartition3()
#                print result
#                assert result.find('false') > 0
#
if __name__ == '__main__':
	unittest.main()
