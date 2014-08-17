#!/usr/bin/python
import cgitb,cgi
from myExceptions import *
from checkLogin import checkLogin
from registerUser import registerUser


cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
password  = form.getvalue('password')
lastname = form.getvalue('lastname')
firstname = form.getvalue('firstname')
interests = form.getvalue('interests')
operation  = form.getvalue('operation')
#print type(operation)

try:
	if operation is None:
		raise myException("no operation chosen")
	if(operation=="login"):
		if password is None or username is None:
			raise myException("form not filled","<loginResult>false</loginResult>")
		holder=checkLogin(username,password)
	elif(operation=="register"):
		if password is None or username is None or lastname is None or firstname is None or interests is None:
			raise myException("form not filled","<registerUser2Result>false</registerUser2Result>")
		holder=registerUser(username,password,firstname,lastname,interests)
except myException, (instance):
	holder=instance.parameter
except (RuntimeError, TypeError, NameError):
	holder="error"

print "Content-type: text/xml"
print
print holder
