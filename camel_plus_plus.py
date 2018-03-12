'''
Camel++

With every variable name in camelCase haha
Sorry hardcore python devs

Schoperation 03/05/2018
'''

# Imports
from player import *
from journey import *
from natives import *
import art

def main():

	# Create player
	player = Player()

	# Ask if the user is using Windows or not
	print("Please enter the number corresponding to your OS: \n")
	print("\t1. Windows")
	print("\t2. MacOS/Linux\n")

	osInt = int(input("#"))

	if osInt == 1:
		player.usingWindows = True
	else:
		player.usingWindows = False

	# Clear screen
	player.clearScreen()

	# Print Welcome message
	welcomeMessage()

	player.clearScreen()

	# Difficulty selection
	diff = difficultySelection()

	# Create journey and natives
	trip = Journey()
	natives = Natives()

	# Decipher difficulty
	if diff == 1:
		trip.setLength(200)
	elif diff == 2:
		trip.setLength(500)
	elif diff == 3:
		trip.setLength(900)
	elif diff == 4:
		trip.setLength(1800)
	else:
		customMiles = int(input("How long of a trip? Whole numbers only. "))
		trip.setLength(customMiles)

	# Main loop TODO
	while True:

		
		if player.failed:
			break
		else:
			trip.beginTurn(player, natives, True)

def welcomeMessage():

	art.logo()
	print("You have recently been captured by an undocumented, cannibalistic tribe of pigmies.")
	print("Fortunately, you have managed to escape them.")
	print("Unfortunately, that is with a puny canteen, a pinch of dosh, and... a camel.")
	print("The pigmies definitely know of your escape and are not far behind you.")
	print("Good luck, you're going to run out of it immediately.")
	input("\nPress Enter to Continue...")

def difficultySelection():

	art.difficulty()
	print("\nBefore you begin, choose your journey.")
	print("Longer journeys mean more chances for miracles and pure bullcrap. Mostly bullcrap.\n")
	print("\t1. Puny (200 miles)")
	print("\t2. Decent (500 miles)")
	print("\t3. Pretty Long (900 miles)")
	print("\t4. Epic (1800 miles)")
	print("\t5. Custom (??? miles)\n")
	difficulty = int(input("Pick a number: "))

	return difficulty

main()