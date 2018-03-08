'''
Class for the pigmies chasing the player.
'''

import random

class Natives():

	def __init__(self):

		self.milesTraveled = -15
		self.milesIncrement = 0

	def travel(self):

		# Randomly decide whether to travel a lot or not at all
		howFar = random.randint(1, 3)

		if howFar == 1:
			self.milesIncrement = random.randint(5, 10)
		elif howFar == 2:
			self.milesIncrement = random.randint(10, 15)
		else:
			self.milesIncrement = random.randint(15, 20)

		self.milesTraveled += self.milesIncrement