#!/usr/bin/python
from cleanHtml import *
def cleanInput(inputdata):
	return sanitize_html(inputdata)	

def test():
	data="<javascript>tester</javascript>"
	print cleanInput(data)

if __name__ == '__main__':
	test()
