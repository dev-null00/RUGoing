#!/usr/bin/python
import cgitb,cgi
from getEvents import getEvents
from searchEvents import searchEvents
from getRecommendedEvents import getRecommendedEvents
from modifyUser import modifyUser
from rateEvent import rateEvent

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
username = form.getvalue('username')
operation = form.getvalue('operation')
query = form.getvalue('query')
if(operation=="upcoming"):
	holder=getEvents()
	print "Content-type: text/xml"
	print
	print holder
elif(operation=="search"):
	holder=searchEvents(query)
	print "Content-type: text/xml"
	print
	print holder
elif(operation=="recommend"):
	holder=getRecommendedEvents(username)
	print "Content-type: text/xml"
	print
	print holder
elif(operation=="modify"):
	firstname = form.getvalue('firstname')
	lastname = form.getvalue('lastname')
	oldpassword = form.getvalue('oldpassword')
	newpassword = form.getvalue('newpassword')
	interests = form.getvalue('interest')
        holder=modifyUser(username,oldpassword,newpassword,firstname,lastname,interests)
        print "Content-type: text/xml"
        print
        print holder
elif(operation=="rate"):
	eventID = form.getvalue('eventID')
	rating = form.getvalue('rating')
	holder=rateEvent(username, eventID, rating)
	print "Content-type: text/xml"
	print
	print holder
