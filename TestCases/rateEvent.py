#!/usr/bin/python

# post xml soap message

import httplib
#from xml.dom import minidom
from xml.dom.minidom import parse, parseString

def rateEvent(username, eventID, rating):
# a "as lighter as possible" soap message:
 SM_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <login xmlns="http://tempuri.org/">
      <username>""" + username + """</username>
      <eventID>""" + eventID + """</eventID>
      <rating>""" + rating " """</rating>
     </login>
  </soap12:Body>
</soap12:Envelope>
"""
 SoapMessage = SM_TEMPLATE%()
###construct and send the header
 webservice = httplib.HTTPS("192.168.56.102")
 webservice.putrequest("POST", "/uiinter/Service.asmx")
 webservice.putheader("Host", "192.168.56.100")
 webservice.putheader("User-Agent", "Python post")
 webservice.putheader("Content-type", "application/soap+xml; charset=\"UTF-8\"")
 webservice.putheader("Content-length", "%d" % len(SoapMessage))
 webservice.putheader("SOAPAction", "\"\"")
 webservice.endheaders()
 webservice.send(SoapMessage)
## get the response
 statuscode, statusmessage, header = webservice.getreply()
 res = webservice.getfile().read()
# xmldoc = parseString(res)
 #for node in xmldoc.getElementsByTagName('loginResult'):  # visit every node <loginResult />
 # hold=node.firstChild.nodeValue
# output=xmldoc.getElementsByTagName('loginResult')[0].firstChild.nodeValue
 return res
 
 def test():
 user="tester"
 passw="test"
 print rateEvent(user,eventID, rating)
 user="tester"
 passw="test"
 print ratEvent(user,eventID, rating)
