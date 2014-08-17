import unittest
import registerUser

class RegisterUserTestCase(unittest.TestCase):
	def setUp(self):
		self.username = "snegala"
		self.password = "rutgers"
		self.lastname = "gala"
		self.firstname = "sneha"
		self.interests = "basketball"


	def runTest(self):
		result=registerUser.registerUser(self.username,self.password,self.firstname,self.lastname,self.interests)
		assert result.find('true') > 0


class ReregisterUserTestCase(unittest.TestCase):
        def setUp(self):
                self.username = "snegala"
                self.password = "rutgers"
                self.lastname = "gala"
                self.firstname = "sneha"
                self.interests = "basketball"


        def runTest(self):
                result=registerUser.registerUser(self.username,self.password,self.firstname,self.lastname,self.interests)
                assert result.find('false') > 0


class InvalidUserNameTest(unittest.TestCase):
	def setUp(self):
		self.username = ""
		self.password = "sda"
		self.lastname = "sda"
		self.firstname = "sda"
		self.interests = "sda"

	def runTest(self):
		result=registerUser.registerUser(self.username,self.password,self.firstname,self.lastname,self.interests)
		assert result.find('false') > 0

if __name__ == '__main__':
	unittest.main()
