'''
Camel++

With every variable name in camelCase haha
Sorry hardcore python devs

Schoperation 03/05/2018
'''

# Imports
from player import *

def main():

	# Create player
	player = Player()

	# Ask if the user is using Windows or not
	print("Please enter the number corresponding to your OS: \n")
	print("\t1. Windows")
	print("\t2. MacOS/Linux\n")

	osInt = int(input(">"))

	if osInt == 1:
		player.usingWindows = True
	else:
		player.usingWindows = False

	# clear screen
	player.clearScreen()

main()