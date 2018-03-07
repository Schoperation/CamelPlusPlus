'''
The class dealing with the player and the camel.
'''

import os
import random

class Player():
	
	def __init__(self):
		""" Variables more about the player itself """
		self.milesTraveled = 0
		self.gold = 2
		self.thirst = 0
		self.location = "DESERT"
		self.failed = False

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

	""" Methods to deal with the player """
	def travel(self, fullSpeed):

		if fullSpeed:
			self.milesTraveled += random.randint(10, 20)
			self.thirst += random.randint(1, 2)
			self.camelTiredness += random.randint(2, 4)
		else:
			self.milesTraveled += random.randint(5, 12)
			self.thirst += random.randint(1, 2)
			self.camelTiredness += random.randint(1, 2)

	def quenchThirst(self):

		if self.canteenSips > 0:
			self.thirst -= 3
			self.canteenSips -= 1
			print("Ahhhh, how refreshing.")
		else:
			print("Not even a measly drop of water is left.")