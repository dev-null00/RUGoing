#!/usr/bin/python
import cgitb,cgi
from checkLogin import checkLogin
from checkLogin import testPage

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
password  = form.getvalue('password')

try:
	holder=checkLogin(username,password)
except (RuntimeError, TypeError, NameError):
	holder="error"

print "Content-type: text/xml"
print
print "<result>"
print holder
print "</result>"
#holder=testPage() 
#return str(holder)
#print "Content-type: text/html"
