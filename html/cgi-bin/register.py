#!/usr/bin/python
import cgitb,cgi
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

try:
	holder=registerUser(username,password,firstname,lastname,interests)
except (RuntimeError, TypeError, NameError):
	holder="error"

print "Content-type: text/xml"
print
#print "<result>"
print holder
#print "</result>"
#holder=testPage() 
#return str(holder)
#print "Content-type: text/html"
