# Project 5
# Author: Charlotte UWIMANA
# 1 December 2017

class Player(object):
	#docstring for player
	# player name
	name = ""
	# player score
	score = 0
	# player current location
	current_loc = ""
	# number of moves made by player btn locations
	move_count = 0
	# collections
	inventory = []

	def __init__(self, name):
		self.name = name	
	# add player's score
	def add_score(self, points):
		self.score+=points
	# update player location
	def update_loc(self, loc):
		self.current_loc = loc
	# updating move counts
	def move_counter(self):
		self.move_count +=1;
	# adding new inventory
	def add_to_inventory(self, item):
		self.inventory.append(item);
	# player drops an item on a location
	def drop(self, item):
		if item in self.inventory:
			self.inventory.remove(item)
	# player take an item from the location 
	# adds an item to inventory
	def take(self, item):
	    self.inventory.append(item)
	# player uses and item
	def use(self, item):
	    pass












		
		
