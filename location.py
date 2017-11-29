# Project5
# Author: Charlotte UWIMANA
# 1 December 2017
class Locale(object):
	#docstring for locale
	# place name
	name = ""
	# place description before
	desc = ""
	# place description after
	new_desc = ""
	# false if not visited, true otherwise
	visited = False
	# false when not search, true otherwise
	searched = False
	# list of items at a location
	items = []
	def __init__(self, name, desc, items=[]):
		self.name = name
		self.desc = desc
		self.items =items
		self.desc_after = " You returned to " +name+ "."
	# player drop an item to this place
	def drop(self, item):
		self.items.append(item)
	# player take an item from this place
	def take(self, item):
		self.inventory.remove(item)
