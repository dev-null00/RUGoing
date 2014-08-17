#!/usr/bin/python
import cgitb,cgi,os

cgitb.enable()
form = cgi.FieldStorage()
# A nested FieldStorage instance holds the file
fileitem = form['image']
eventID = form.getvalue('eventID')

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('../eventImages/'+eventID+'_'+ fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
#print """\
#Content-Type: text/html\n
#<html><body>
#<p>%s</p>
#</body></html>
#""" % (message,)`
print "Content-type: text/html"
print
print message
