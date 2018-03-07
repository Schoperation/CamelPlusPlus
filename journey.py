'''
This takes care of the journey that the player must go through.
Processes turns, shows menus, rolls for random events, etc.
'''

from natives import *
from player import *
import random
import time
import art

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
		# TODO put a visual of the player's location on this line
		self.printStatus(player, natives)
		self.printMainMenu()
		self.processMenuChoice(player, natives)

	def printStatus(self, player, natives):

		print("STATUS:\n")

		# URGENT
		# Thirst
		if player.thirst >= 6:
			print("!!! You are very thirsty. !!!")
		elif player.thirst >= 3:
			print("!!! You are starting to feel thirsty. !!!\n")

		# Camel
		if player.camelTiredness >= 8:
			print("!!! Your camel is very fatigued. It could die soon if it doesn't rest soon. !!!")
		elif player.camelTiredness >= 4:
			print("!!! Your camel is showing signs of fatigue. !!!\n")

		# Location
		print("Currently in", player.location)

		# Day
		if self.day == 1:
			print("You've been traveling for", self.day, "day.")
		else:
			print("You've been traveling for", self.day, "days.")

		# Money
		print("You have", player.gold, "gold coins in your pocket.")

		# Miles
		print("You have traveled", player.milesTraveled, "miles out of the", self.miles, "mile journey.")

		# Natives
		distanceBehind = player.milesTraveled - natives.milesTraveled
		estimateHigh = distanceBehind + random.randint(2, 10)
		estimateLow = distanceBehind - random.randint(2, 10)
		print("You estimate the natives to be between", estimateLow, "and", estimateHigh, "miles behind you.")

	def printMainMenu(self):

		print("\nWhat would you like to do?\n")

		print("\t1. Travel at moderate speed.")
		print("\t2. Travel at full speed.")
		print("\t3. Scout the surrounding area.")
		print("\t4. Rest for the day.")
		print("\t5. Take a sip out of your canteen.")
		print("\t6. Accept your fate.")

	def processMenuChoice(self, player, natives):

		# Ask for input
		choice = int(input("#"))

		# Decipher input
		if choice == 1:
			player.travel(False)
			natives.travel()
		elif choice == 2:
			player.travel(True)
			natives.travel()
		elif choice == 3:
			natives.travel() # TODO
		elif choice == 4:
			natives.travel() # TODO
		elif choice == 5:
			player.quenchThirst()
			time.sleep(2)
			print("What now?")
			self.processMenuChoice(player, natives)
		elif choice == 6:
			print("Some may call you cowardly, others brave for doing this.")
			print("But hey, we all make choices.")
			player.failed = True
		else:
			print("Huh? I do not understand your command.")
			time.sleep(2)
			self.processMenuChoice(player, natives)


		# Check if loser
		self.checkLoser(player, natives)

		# Check if winner
		if player.milesTraveled >= self.miles and not player.failed:
			player.clearScreen()
			art.congratulations()
			print("You've made it through the entire", self.miles, "mile journey!")
			print("You've escaped the hungry pigmies and on your way to a new life.")
			input("\nPress Enter to Finish.")
			player.failed = True


	def checkLoser(self, player, natives):

		# Natives caught up?
		if natives.milesTraveled >= player.milesTraveled:
			player.clearScreen()
			art.gameOver()
			player.failed = True
			print("The pigmies have caught up with you and made you into a creamy soup.")
			print("You hope they die of disgust. But unfortunately, that's not how they roll.")
		# Died of thirst?
		elif player.thirst >= 8:
			player.clearScreen()
			art.gameOver()
			player.failed = True
			print("Not even a teardrop could save you from your death by dehydration.")
		# Camel died of exhaustion
		elif player.camelTiredness >= 10:
			player.clearScreen()
			art.gameOver()
			player.failed = True
			print("Your camel couldn't handle the cruel strain you put onto it, and died of exhaustion.")