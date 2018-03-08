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
	""" Checking inventory of the player. """
	def checkInventory(self):

		print("You've got", self.gold, "gold coins.")
		#print inventory here, when implemented

	""" Travel. """
	def travel(self, fullSpeed):

		miles = 0

		if fullSpeed:
			miles = random.randint(10, 20)
			self.thirst += random.randint(1, 2)
			self.camelTiredness += random.randint(2, 3)
		else:
			miles = random.randint(5, 12)
			self.thirst += random.randint(1, 2)
			self.camelTiredness += random.randint(1, 2)

		self.milesTraveled += miles
		print("You've traveled an extra", miles, "miles.")

	""" Sipping from the canteen. """
	def quenchThirst(self):

		if self.canteenSips > 0:
			self.thirst -= 3
			self.canteenSips -= 1
			print("Ahhhh, how refreshing.")
			if self.canteenSips == 1:
				print(self.canteenSips, "measly sip left.")
			else:
				print(self.canteenSips, "sips left.")
		else:
			print("Not even a measly drop of water is left.")

	""" Resting for the day. """
	def rest(self):

		self.camelTiredness -= 5
		self.thirst += 1

		print("You've rested along with your camel.")

	""" Scout the area. Lotta random. """
	def scout(self):
		# will have more stuff soon tm
		print("Scouting complete.")