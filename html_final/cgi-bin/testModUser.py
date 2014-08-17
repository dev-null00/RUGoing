import unittest
import modifyUser

#ModifyUser 2 test cases

#1. Test case for correct username and password. Allows user to modify her password.
#2. Test case for correct username and wrong password does not allow the user to modify.
#3. Test case wrong username does not allow the user to modify.

class ModifyUserTestCase(unittest.TestCase):
        def setUp(self):
                self.username = "snegala"
                self.oldpassword = "rutgers"
                self.newpassword = "rutgers123"
                self.lastname = "gala"
                self.firstname = "sneha"
                self.interests = "basketball"


        def runTest(self):
                result=modifyUser.modifyUser(self.username,self.oldpassword,self.newpassword,self.firstname,self.lastname,self.interests)
                assert result.find('true') > 0

class ExceptionTest(unittest.TestCase):
        def setUp(self):
                self.username = "snegala"
                self.oldpassword = "wrong"
                self.newpassword = "cantchange"
                self.lastname = "gala"
                self.firstname = "sneha"
                self.interests = "basketball"

        def runTest(self):
                result=modifyUser.modifyUser(self.username,self.oldpassword,self.newpassword,self.firstname,self.lastname,self.interests)
                assert result.find('false') > 0

if __name__ == '__main__':
        unittest.main()
