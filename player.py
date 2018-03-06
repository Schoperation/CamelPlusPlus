'''
The class dealing with the player and the camel.
'''

import os

class Player():
	
	def __init__(self):
		""" Variables more about the player itself """
		self.milesTraveled = 0
		self.thirst = 0

		""" Camel """
		self.camelTiredness = 0

		""" Canteen """
		self.canteenSips = 3
		self.maxCanteenSips = 3

		""" Their operating system """
		self.usingWindows = False

	""" Clear the screen """
	def clearScreen(self):

		if self.usingWindows:
			os.system("cls")
		else:
			os.system("clear")