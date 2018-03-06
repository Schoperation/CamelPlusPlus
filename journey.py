'''
This takes care of the journey that the player must go through.
Processes turns, shows menus, rolls for random events, etc.
'''

from natives import *
from player import *
import random

class Journey():

	def __init__(self):

		self.day = -1
		self.miles = 0
		self.chanceForMiracles = 0.0
		self.chanceForBullCrap = 0.0

	def setLength(self, value):

		self.miles = value

		if value == 200:
			self.chanceForBullCrap = 0.05
			self.chanceForMiracles = 0.05
		else:
			self.chanceForMiracles = 0.00015 * value
			self.chanceForBullCrap = 0.00020 * value


	""" The actual turns. Uses printMenu and printStatus """
	def beginTurn(self, player, natives, incDay):

		if incDay:
			self.day += 1

		player.clearScreen()
		self.printStatus(player, natives)
		self.printMainMenu()

	def printStatus(self, player, natives):

		print("STATUS:\n")

		# Day
		if self.day == 1:
			print("You've been traveling for", self.day, "day.")
		else:
			print("You've been traveling for", self.day, "days.")

		# Money
		print("You have", player.gold, "gold coins in your pocket.")

		# Thirst
		if player.thirst >= 6:
			print("You are very thirsty.")
		elif player.thirst >= 3:
			print("You are starting to feel thirsty.")

		# Camel
		if player.camelTiredness >= 8:
			print("Your camel is very fatigued. It could die soon if it doesn't rest soon.")
		elif player.camelTiredness >= 4:
			print("Your camel is showing signs of fatigue.")

		# Miles
		print("You have traveled", player.milesTraveled, "miles out of the", self.miles, "journey.")

		# Natives
		distanceBehind = player.milesTraveled - natives.milesTraveled
		estimateHigh = distanceBehind + random.randint(2, 10)
		estimateLow = distanceBehind - random.randint(2, 10)
		print("You estimate the natives to be between", estimateLow, "and", estimateHigh, "miles behind you.")

	def printMainMenu(self):

		print("\nWhat would you like to do?\n")

		print("\t1. Travel at a moderate speed.")
		print("\t2. Travel at full speed.")
		print("\t3. Scout the surrounding area.")
		print("\t4. Rest for the day.")
		print("\t5. Take a sip out of your canteen.")
		print("\t6. Accept your fate.")