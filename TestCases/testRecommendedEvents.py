import unittest
import getRecommendedEvents
from xml.dom.minidom import parse, parseString

class rateEventTestCaseMinBoundary(unittest.TestCase):
 def setUp(self):
    pass
    self.username = "nanoer2"
    
 def tearDown(self):
    pass

 def runTest(self):
   result=getRecommendedEvents.getRecommendedEvents(self.username)
   xmldoc = parseString(result)  
   node=xmldoc.getElementsByTagName('eventDataDB')
   assert len(node) > 0

class invalidUserTestCase(unittest.TestCase):
 def setUp(self):
    self.fakeusername = "notarealuser"

 def runTest(self):
   result=getRecommendedEvents.getRecommendedEvents(self.fakeusername)
   xmldoc = parseString(result)
   node=xmldoc.getElementsByTagName('eventDataDB')
   assert len(node) is 0
class checkInputLimitTestCase(unittest.TestCase):
 def setUp(self):
    self.usernametoolong = "notarealuser123456789"

 def runTest(self):
   result=getRecommendedEvents.getRecommendedEvents(self.usernametoolong)
   xmldoc = parseString(result)
   node=xmldoc.getElementsByTagName('eventDataDB')
   assert len(node) is 0


if __name__ == '__main__':
    unittest.main()

