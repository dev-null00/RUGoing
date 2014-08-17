import unittest
import registerUser
#Test1:To validate the user data (username, password, firstname, lastname, interest), provided during registration

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
		
#Test2: To reject acception of the user data (username, password, firstname, lastname) provided by user if it is already existing in the user database   

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

#Test3: To invalidate the incorrect values provided for username, password, firstname, lastname, interest example "blank"

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
