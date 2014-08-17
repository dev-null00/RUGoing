import unittest
import modifyUser

#ModifyUser 2 test cases

#1. Test case for correct username and password. Allows user to modify her password.
#2. Test case for correct username and wrong password does not allow the user to modify.

class ModifyUserTestCase(unittest.TestCase):
	def setUp(self):
#		pass
		self.username = "snegala"
		self.password = "rutgers"
		self.lastname = "gala"
		self.firstname = "sneha"
		self.interests = "basketball"

#	def tearDown(self):
#		pass

	def runTest(self):
		result=modifyUser.modifyUser(self.username,"rutgersece",self.firstname,self.lastname,self.interests)
		assert result.find('true') > 0

class ExceptionTest(unittest.TestCase):
	def setUp(self):
		self.username = "snegala"
		self.password = "rutgers1234"
		self.lastname = "gala"
		self.firstname = "sneha"
		self.interests = "basketball"

	def runTest(self):
		result=modifyUser.modifyUser(self.username,self.password,self.lastname,self.interest)
		assert result.find('false') > 0

if __name__ == '__main__':
	unittest.main()
