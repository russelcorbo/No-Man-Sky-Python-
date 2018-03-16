#!usr/bin/env python
# -*- coding: utf-8 -*-

import random
from random import randint
import celestialObj
import planetMoon
import species
import time
import string
import os
import sys

# is there a way to clear the above field after going through it?


oxides = ['iron', 'titanium', 'zinc']
isotopes = ['carbon', 'plutonium', 'thiamium9']
silicates = ['chrysonite', 'heridium', 'platinum']
neutrals = ['aluminum', 'copper', 'emeril', 'gold', 'iridium', 'nickel']
preciousmetals = ['calium', 'omegon', 'radnox']
alloys = ['lemmium', 'terumin', 'herox', 'magmox']

pwrelt = ['iron', 'titanium', 'zinc', 'carbon', 'plutonium', 'thiamium9', 'chrysonite', 'heridium', 'platinum', 'aluminum', 'copper', 'emeril', 'gold', 'iridium', 'nickel', 'calium', 'omegon', 'radnox', 'lemmium', 'terumin', 'herox', 'magmox', 'nothing']
itemBag = []

print("*******"
	  "\n"
	  "*******"
	  "\n"
	  "Welcome to the python powered text version of No Man Sky!"
	  "\n"
	  "*******"
	  "\n"
	  "*******")

user_name = input("First, what is your name?: ")
print("\n"
			"\n")
print("So your name is " + user_name)
print("\n"
	  "\n")
time.sleep(3)

print("There are three factions: "
	  "\n"
			"\n"
			"engineer warrior and doctor"
			"\n"
			"\n"
			"engineer excels in learning abilities "
			"\n"
			"\n"
			"warrior excels in battling and defense abilities "
			"\n"
			"\n"
			"doctor excels in healing abilities "
			"\n"
			"\n")
faction = input("Which faction do you choose? :")

print("You have chosen " + faction)
#TODO: class for planets + minerals, function to randomize them. class for your ship
time.sleep(2)

if faction == "engineer":
	print("As an engineer you are smarter than the average bear"
		  " you have a proclivity for algorithms and finding your way "
		  "out of a hairy situation.")
if faction == "warrior":
	print("As a warrior you are strong and cunning, crushing your enemies.")
if faction == "doctor":
	print("As a doctor you care more about the worlds around you.")
if faction != "engineer" or "warrior" or "doctor":
	print("ಠ_ಠ")

time.sleep(3)

'''
TODO: Create the differences between engineer doctor and warrior.

engineer:


doctor:


warrior:



'''


#print("Your starting spacecraft is a {} which requires {} Aluminum and {} Iron to disembark".format(spaceCraft))

# need to save elements in variable names
# perhaps also a 'bag' of elements

class spaceCraft ():
	'''
	class for creating spacecrafts.
	within this class are pieces such as:
		name = the name of the craft
		value = the amount of space coins needed to purchase one. Coins use § symbol
		speed = how fast can this craft go. I havent decided yet how this will be calculated, but i know this number will be a float

		pwrelt = which element will power this ship. these elements will be a string and will need to be collected prior to disembarkation.
		defenses = also will be a string. Your ship is primarily an exploration vehicle, but in the field you may encounter unfriendlies and will need a way to protect yourself.
	'''
	def __init__(self,
				 name,
				 max_fuel,
				 origin,
				 destination,
				 pwrelt1,
				 pwrelt2='',
				 defenses='',
				 value='',
				 speed='',):
			self.name = name
			self.max_fuel = max_fuel
			self.origin = origin
			self.destination = destination
			self.pwrelt = pwrelt1
			self.pwrelt = pwrelt2
			self.defenses = defenses
			self.value = value
			self.speed = speed

			current_fuel = 0
			print(current_fuel)

	def fuel_amount(self):
		"""This will tell the user if they have enough fuel."""
		current_fuel = self.max_fuel
        print("Ship filled up. You have {} gallons of fuel".format(
            self.max_fuel))

	def description(self):
		"""This will tell the user what kind of craft they have."""
		print("Your ship is a {}, which requires {} Aluminum"
			  " and {} Iron".format(
				self.name,
				self.pwrelt1,
				self.pwrelt2))

	def destination_range(self):
		"""Fuel and Destination."""
		if self.destination < self.origin:
            print("You need to find resources to fuel your craft.")
        if self.destination >= self.origin:
            print("You are cleared for takeoff.")


'''
TODO: Different spacecrafts and their features:
	Shuttles - pwrelt? - how quickly is it used up? -
	Fighter
	Explorer
	Hauler
	Exotic
	Freighter

'''

class elements ():
	'''
	## this class may be able to be scrapped as i think doing a kwarg list may be better suited for this.
	this class will go over the different types of minerals that you may find on different worlds.
	It will be broken up into:
		name = the name of the mineral, obviously a string.
		rarity = how rare the mineral is will determine how often you can find it. perhaps a value of 1-4.
		pwr = how powerful is it, perhaps another int.
	'''
	def __init__(self, name='', rarity='', pwr=''):
		self.name = name=''
		self.rarity = rarity=''
		self.pwr = pwr=''



	#scanques = input("Use your scanner to search nearby? "
	#								 ":")
	#								 if input == "y":
	#								 	print("Lets scan your surroundings")
	#								 if "n":
	#								 	print("Sit wait and die i guess.")


def disembark():
	'''
	This allows the player to take off once minerals have been found. It needs to be a check
 for whats in the itemBag, if certain elements are not among your list then you must continue searching
	Can certain ships need two elements to power, choose two different ones per ship type.
 	 	'''
 	if itemBag == ["iron", "iron"]:
 		print("You are cleared for disembarkation")
 	else:
 		print("You must continue to collect more elements")
	print("\n"
				"Now that you’ve found all of the elements that you need, you may disembark "
 			  "\n"
 				"\n"
 				"...thrusters firing..."
 				"\n"
 				"\n"
 				"You are now able to leave the planet you’re on"
 				"\n"
 				"\n"
 				" Now what would you like to do? ")
	whereTo = input("Type 'explore' to explore your current solar system "
				"\n"
				"\n"
				if whereTo == 'explore':
					exploreCurrent()
				"Type 'view' to view the items in your bag "
				"\n"
				"\n"
				if whereTo == 'view':
					print(itemBag)
				"Type ‘fuel’ to check your fuel status "
				"\n"
				"\n"
				if whereTo == 'fuel':
					fuelGauge()
				"Type 'starmap' to see your star map for neighboring solar systems"
				"\n"
				"\n"
				if whereTo == 'starmap':
					starmap()
				"or Type ‘descend’ to land back onto the planet you were just on")


def exploreCurrent():
	'''This function will have planets moons and space stations within it, and will randomize the amount for the current solar system'''



def starmap():
	'''This function will randomize letters and numbers to come up with a set amount for the top 5 nearest star systems, as well as how far they are'''


def random_item(choice_list):
    """Random area."""
    comp_pick = randint(0, len(choice_list) - 1)
    return choice_list[comp_pick]


def scanSurroundings():
	comp_pick = random_item(pwrelt)
	print("Your craft has crashed on an unknown planet")
	print("In order to continue with your exploratory mission, you must search the planet for elements to power your craft")
	run = True
	while run:
		players_pick = input("Would you like to scan? ")
		if players_pick == "yes":
			print("Your scanner has found {}".format(comp_pick))
			if comp_pick == "nothing":
				print("There is nothing nearby")
			addItem = input("Would you like to add {} to your bag? ".format(comp_pick))
			if addItem == "yes":
				print("item added")
				itemBag.append(comp_pick)
			if addItem == "no":
				print("item tossed")
		players_pick = input("Would you like to scan? ")
		if players_pick == "yes":
			print("Your scanner has found {}".format(comp_pick))
			addItem2 = input("Would you like to add {} to your bag? ".format(comp_pick))
		if addItem2 == "yes":
			print("item added")
			itemBag.append(comp_pick)
		if players_pick == "no":
			print("You need to scan to find elements")
		run = False
		nextStep = input("Now that you have some elements, what would you like to do? "
										 "\n"
										 "\n"
										 "Scan for more elements? "
										 "\n"
										 "\n"
										 "Attempt to disembark? "
										 "\n"
										 "\n"
										 "Search for life? ")
		if nextStep == "scan for more elements":
				scanSurroundings()
		if nextStep == "attempt disembark":
				disembark()
		if nextStep == "search for life":
				searchForLife()
		if nextStep == "q":
				sys.exit()

# perhaps add a "would you like to scan again option?"
# add "nothing" to list. if "nothing is found then scanSurroundings should end"
# there should be a max amount of items in the itemBag list
# i want to make it so that not only does it pop out a random mineral but it chooses a random amount found


scanSurroundings()
disembark()


def whereTo():
	'''
	This would allow a user to choose a selected path
	'''

def hyperSpace():
	'''This allows user to go hyperspace'''


def searchForLife():
	'''This allows the player to search for flora or fauna'''
	userLifeScan = input("Would you like to scan for life?")
	if userLifeScan == "yes":




'''
origin planet X
Once you find the elements you need in allotted time you have several options for next solar system jump depending on your ship.

different solar systems may have planets and moons(elements and supplies for free), life to fill your catalog, space stations(you can buy supplies, or a new ship, or sell supplies and elements)

beacons are for quests which you can choose to accept or not. beacons will appear at random and once you accept them you will follow them to said place as long as you have enough power/elements. quests will lead to freebies such as rare elements or ruins to sell to upgrade your ship.

star systems will sometimes contain planets and moons. these will be at random and will hopefully be developed into a neural network to give you an infinite number of star systems and alien life to fill your database.

 naming structure:
 	star systems will be named for you by a random word containing letters and numbers.
 	planets that you explore will be up to player to name.
 	aliens will also be up to player to name. player will be given a description of creature

concerns and future:
	how will light years be determined?
	look into databases
	how can you randomize aliens?
	'''
