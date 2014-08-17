#!/usr/bin/python
import cgitb,cgi
import os
from myExceptions import *
from getEventInfo import getEventInfo
from xml.dom.minidom import parse, parseString



cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
eventID = form.getvalue('eventID')
holder=getEventInfo(eventID)


#create the dynamic html page
#need to include the rate 
photo='''
	<form method="post" enctype="multipart/form-data" action="/cgi-bin/saveFile.py">
		<a> Upload Image</a> 
		<input type="file" accept="image/gif,image/jpeg" NAME="image">
		<input type="hidden" name="eventID" id="eventID" value="''' + eventID + '''" />
		<br>
		<input type="submit" value="Submit">
	</form>
'''
facebookComments=""" 
<div id="facebookBlock">
	<script src="http://connect.facebook.net/en_US/all.js#appId=fbc8e06287e79e311aab5879f84e4119&amp;xfbml=1"> </script>
	<div id="fb-root"> </div>
	<fb:comments width="425"> </fb:comments>
</div>
"""
header="""<head>
<!--yui-->
		<link rel="stylesheet" type="text/css" href="js/yui/build/fonts/fonts-min.css" /> 
		<link rel="stylesheet" type="text/css" href="js/yui/build/tabview/assets/skins/sam/tabview.css" /> 
		<link rel="stylesheet" type="text/css" href="js/yui/build/datatable/assets/skins/sam/datatable.css" /> 
		<link rel="stylesheet" type="text/css" href="js/yui/build/carousel/assets/skins/sam/carousel.css" />
		<script type="text/javascript" src="js/yui/build/yahoo-dom-event/yahoo-dom-event.js"></script> 
		<script type="text/javascript" src="js/yui/build/element/element-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/tabview/tabview-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/datasource/datasource-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/datatable/datatable-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/connection/connection-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/yahoo-dom-event/yahoo-dom-event.js"></script> 
		<script type="text/javascript" src="js/yui/build/autocomplete/autocomplete-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/utilities/utilities.js"></script> 
		<script type="text/javascript" src="js/yui/build/container/container_core-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/menu/menu-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/resize/resize-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/layout/layout-min.js"></script> 
		<script type="text/javascript" src="js/yui/build/carousel/carousel-min.js"></script> 
<!--jquery -->
                <script src="js/jquery/jquery-1.4.2.min.js" type="text/javascript"></script>
                <script type="text/javascript" src="js/jquery/jquery.raty.min.js"></script>
                <script type="text/javascript" src="js/rate.js"></script>
<!--custom functions-->
		<script language="JavaScript" src="js/cookies.js"></script> 
		<script language="JavaScript" src="js/rowexp.js"></script> 
		<script type="text/javascript" src="js/dataTables/createUpcomingEvents.js"></script>
		<script type="text/javascript" src="js/dataTables/createSearchEvents.js"></script>
		<script type="text/javascript" src="js/dataTables/createrecommendedEvents.js"></script>
		<script type="text/javascript" src="js/photo.js"></script> 
<!--custom style -->
		<link rel="stylesheet" type="text/css" href="style/theme.css" /> 


</head>
"""
xmldoc = parseString(holder)
eventname=xmldoc.getElementsByTagName('name')[0].childNodes[0].nodeValue
hashtag=xmldoc.getElementsByTagName('hashtag')[0].childNodes[0].nodeValue
synopsis=xmldoc.getElementsByTagName('synopsis')[0].childNodes[0].nodeValue
timeofevent=xmldoc.getElementsByTagName('timeofevent')[0].childNodes[0].nodeValue
location=xmldoc.getElementsByTagName('location')[0].childNodes[0].nodeValue
locationNoSpace=location.replace(" ","+")
locationNoSpace=locationNoSpace.replace("&","")

twitter="""
<div id="twitterBlock">
	<script src="http://widgets.twimg.com/j/2/widget.js"></script>
	<script src="js/twitter.js"></script>
	<script>
		runtwitter('"""+eventname+"""','#"""+hashtag+"""');
	</script>
</div>
"""
#change spaces to + signs to have the location link
eventDetails="""
	<table id="eventDetails">
		<tr><td>Event:</td><td>""" + eventname + """</td></tr>
		<tr><td>Synopsis:</td><td>""" + synopsis + """</td></tr>
		<tr><td>Start Time:</td><td>""" + timeofevent + """</td></tr>
		<tr><td>Location:</td><td><a href='http://rumaps.rutgers.edu/?q="""+locationNoSpace+"""'>""" + location + """</a></td></tr>
		<tr><td>Twiter Tag:</td><td>#"""+hashtag + """</td></tr>
		<tr><td>Rate Event:</td><td><div id="click"></div></td></tr>
	</table>
"""
ratebar="""
<div id="click"></div>
"""

photocontainer="""
<div id="photoHolder">
	<div id="photocontainer">
		<ol id="carousel">
"""
fileList=[]
files=os.listdir("../eventImages")
checker=0
for imagefile in files:
	if(imagefile.startswith(eventID+"_")):
		checker=checker+1
		photocontainer=photocontainer+"\t\t\t<li> <img src=\"eventImages/"+imagefile+"\" width=\"75\" height=\"75\"> </li>\n"

photocontainer=photocontainer+"""
		</ol>
	</div>
	<!-- The spotlight container -->
	<div id="spotlight"></div>
</div>
"""

if checker == 0:
	photocontainer=""


rugoinglogo="""
<img src="images/rugoingLogo.jpg" width="296" height="140.75"/>
"""

print "Content-type: text/html"
print
print header +"<body class=\"yui-skin-sam\">\n"+"<div id=\"leftside\">"+rugoinglogo+"</div>\n<div id=\"rightside\">\n"+"<div id=\"top\">\n"+"<div id=\"eventandphotosubmit\">"+ eventDetails + photo +"</div>"+photocontainer+"</div>\n" + "<div id=\"bottom\">" + facebookComments + twitter +"</div>\n</div>\n" + "</body>"
