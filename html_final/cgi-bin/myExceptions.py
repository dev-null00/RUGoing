class myException(Exception):
	def __init__(self, value, mustReturn=""):
		self.parameter ="<error>\n<flag>\ntrue\n</flag>\n<details>\n"+ value + "\n</details>\n</error>"
		self.parameter ="<error>\n<flag>\ntrue\n</flag>\n<details>\n"+ value + "\n</details>\n" + mustReturn + "\n</error>"
#	def __init__(self, value, mustReturn):
#		self.parameter ="<error>\n<flag>\ntrue\n</flag>\n<details>\n"+ value + "\n</details>\n" +mustReturn "\n</error>"
	def __str__(self):
		return repr(self.parameter)
