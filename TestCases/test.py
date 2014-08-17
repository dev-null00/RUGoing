import unittest
import registerUser

class RegisterUserTestCase(unittest.TestCase)
def setUp(self):
    pass
    self.username = "snegala"
    self.password = "rutgers"
    self.lastname = "gala"
    self.firstname = "sneha"
    self.interests = "basketball"

def tearDown(self):
    pass

def runTest(self):
result=registerUser.registerUser(self.username,self.password,self.lastname,self.interest)
assert result == true , 'error occured'

class ExceptionTest(unittest.TestCase)
df setUp(self):
     self.username = "0"
    self.password = "0"
    self.lastname = "0"
    self.firstname = "0"
    self.interests = "0"

    def runTest(self):
result=registerUser.registerUser(self.username,self.password,self.lastname,self.interest)
assert result == false , 'error occured'

if __name__ == '__main__':
    unittest.main()
