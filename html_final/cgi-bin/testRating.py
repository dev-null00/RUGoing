import unittest
import rateEvent

class rateEventTestCaseMinBoundary(unittest.TestCase):
 def setUp(self):
    pass
    self.username = "snegala"
    self.eventID = "12"
    self.rating   = "-2"       #rating should not be negative  
    
 def tearDown(self):
    pass

 def runTest(self):
   result=rateEvent.rateEvent(self.username,self.eventID, self.rating)
   assert result.find('false') > 0

class rateEventTestCaseMaxBoundary(unittest.TestCase):
 def setUp(self):
    pass
    self.username = "snegala"
    self.eventID = "12"
    self.rating   = "12"            # rating should be between 1 and 5
    
 def tearDown(self):
    pass

 def runTest(self):
   result=rateEvent.rateEvent(self.username,self.eventID, self.rating)
   assert result.find('false') > 0


class rateEventTestCaseInvalidEventID(unittest.TestCase):
 def setUp(self):
    pass
    self.username = "snegala"
    self.eventID = "-3"                 #eventID should be positive integer
    self.rating   = "3"
    
 def tearDown(self):
    pass

 def runTest(self):
   result=rateEvent.rateEvent(self.username,self.eventID, self.rating)
   assert result.find('false') > 0


class testRateEvent(unittest.TestCase):
 def setUp(self):
     self.username = "snegala"
     self.eventID = "1"
     self.rating  ="0"

 def runTest(self):
   result=rateEvent.rateEvent(self.username,self.eventID,self.rating)
   assert result.find('true') > 0

if __name__ == '__main__':
    unittest.main()

