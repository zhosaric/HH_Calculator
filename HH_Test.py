import unittest
from HH_Calculator import HandParse

class HandHistoryTests(unittest.TestCase):
    
	def setUp(self):
		handH = HandParse("Hand_History.txt")
	
	def test_if_values_are_equal(self):
		handH = HandParse("Hand_History.txt") 
		values = handH.parseFile()
		self.assertEqual(float(values[0]), 20.00) 
		self.assertEqual(float(values[1]), 19.25)
		self.assertEqual(float(values[5]), 24.26)
		self.assertEqual(float(values[-1])- float(values[0]), 77.40)
	
	def test_if_profits_calculated_correctly(self):
		handH = HandParse("Hand_History.txt")
		values = handH.parseFile()
		profit = 0.00
		for i in range(0,len(values) - 1):
			profit += float(values[i+1]) - float(values[i])
		self.assertEqual(round(profit, 2), 77.40)
		self.assertEqual(profit, handH.calcProfit())
	
	def test_if_profits_iterated_into_list(self):
		handH = HandParse("Hand_History.txt")
		values = handH.parseFile()
		profLi= []
		profit = 0.00
		for i in range(0,len(values) - 1):
			profit += float(values[i+1]) - float(values[i])
			profLi.append(profit)
		self.assertEqual(round(profLi[0], 2), -.75)
		self.assertEqual(profLi, handH.profitList())
		
	def tearDown(self):
	    pass