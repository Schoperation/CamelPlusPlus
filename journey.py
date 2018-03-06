'''
This takes care of the journey that the player must go through.
Processes turns, shows menus, rolls for random events, etc.
'''

import random

class Journey():

	def __init__(self, miles):

		self.miles = miles
