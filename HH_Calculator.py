import sys, string, re

class HandParse(object):
	def __init__(self, filename):
		self.filename = filename
	
	def parseFile(self):
		with open(self.filename, "r") as f:
			text = f.read().replace("\n","")
			m = re.findall('\[ME\] \(\$(.+?) in chips', text)
			return m
	
	def calcProfit(self):
		values = self.parseFile()
		profit = 0.00
		for i in range(0,len(values) - 1):
			profit += float(values[i+1]) - float(values[i])
		return profit
	
	def profitList(self):
		values = self.parseFile()
		profLi= []
		profit = 0.00
		for i in range(0,len(values) - 1):
			profit += float(values[i+1]) - float(values[i])
			profLi.append(profit)
		return profLi

class Tracker(object):
    pass
	
