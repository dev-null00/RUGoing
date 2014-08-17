#!/usr/bin/python

# post xml soap message

import httplib
#from xml.dom import minidom
from xml.dom.minidom import parse, parseString
from datetime import datetime
from datetime import timedelta

def insertEvent(name, location, url, synopsis, category, target_audience, eventtime):
 #check the eventtime range
 ##str_format = "%b %d %Y %H:%M:%S"i
 #get the date for the event
 ##date_from_str = datetime.strptime(eventtime,str_format).date()
 #get the date for today
 ##today_date = datetime.today()
 ##if(date_from_str < today_date):
 ##	return false
 
 #check the number of characters in name
 ##number = len(name)
 ##if(name<6 || number >60):
 ##	return false
 
# a "as lighter as possible" soap message:
 SM_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <insertEvent xmlns="http://tempuri.org/">
      <name>""" + name +"""</name>
      <location>""" +location+ """</location>
      <url>"""+ url + """</url>
      <synopsis>"""+synopsis+"""</synopsis>
      <category>"""+category+"""</category>
      <target_audience>"""+target_audience+"""</target_audience>
      <eventime>"""+eventtime+"""</eventime>
    </insertEvent>
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
 # hold=node.nodeValue
# output=xmldoc.getElementsByTagName('loginResult')[0].nodeValue
 return res

def getText(nodelist):
	rc =[]
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc.append(node.data)
	return ''.join(rc)

def test():
  filexml = open('events_crawled_2010-12-05.xml')
  dom1 = parse(filexml)
  items = dom1.getElementsByTagName("item")
  for item in items:
	name = getText(item.getElementsByTagName("event_title")[0].childNodes)
	name_str = name.encode('ascii', 'ignore')

	location = getText(item.getElementsByTagName("location")[0].childNodes)
	location_str = location.encode('ascii', 'ignore')

	campus = getText(item.getElementsByTagName("campus")[0].childNodes)
    campus_str = campus.encode('ascii', 'ignore')
	
    city = getText(item.getElementsByTagName("city")[0].childNodes)
    city_str = city.encode('ascii', 'ignore')

    url = getText(item.getElementsByTagName("url")[0].childNodes)
    url_str = url.encode('ascii', 'ignore')

    synopsis = getText(item.getElementsByTagName("synopsis")[0].childNodes)
    synopsis_str = synopsis.encode('ascii', 'ignore')

    category = getText(item.getElementsByTagName("category")[0].childNodes)
    category_str = category.encode('ascii', 'ignore')

    item_audience = item.getElementsByTagName("target_audience")
    target_audience = ''
    target_audience_str = ''
    if len(item_audience)>0:
        target_audience = getText(item_audience[0].childNodes)
        target_audience_str = target_audience.encode('ascii', 'ignore')

    eventtime = getText(item.getElementsByTagName("start_time")[0].childNodes)
    eventtime_str = eventtime.encode('ascii', 'ignore')

	location_str = location_str+","+campus_str+" Campus,"+city_str
    print name_str
    print location_str
    print url_str
    print synopsis_str
    print category_str
    print target_audience_str
    print eventtime_str
    #insertEvent(name_str, location_str, url_str, synopsis_str, category_str, target_audience_str, eventtime_str):

def testPage():
 return "page test"

if __name__ == '__main__':
  test()
