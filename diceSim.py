##############################################################################################
# File: diceSim.py      
# Author: Sam Wareing
# Description: script to determine probability of dice rolls using monte carlo simulation
#
#
#
##############################################################################################
import sys
import os
import random

num_simulations = 1000000

def simulateDiceRolls(dice):
	# initialize dictionary to track roll values of dice
	dice_rolls = {} 
	start = len(dice)
	stop = 0
	for di in dice: stop+=di

	for i in range(start, stop+1):
		dice_rolls[i] = 0

	# simulate dice rolls
	for i in range(1, num_simulations+1):
		roll = 0
		for di in dice: 
			roll += random.randint(1, di)
		dice_rolls[roll]+=1

	return dice_rolls

def calculateProbabilty(dice_rolls):
	probability = {} 

	for roll in dice_rolls.keys(): 
		probability[roll] = float(dice_rolls[roll])/num_simulations*100

	return probability


def printResults(probability):
	for roll in probability.keys(): 
		percent = str(probability[roll]) + "%"
		print(str(roll) + ": " + percent)


def usage(): 
    print("diceSim.py # # #....")

if __name__ == "__main__":
	print("let's sim some dice") 

	if len(sys.argv) < 2: 
		usage()
		exit()
	num_dice = len(sys.argv) - 1
	dice = []
	for i in range(1, num_dice+1): dice.append(int(sys.argv[i]))

	print(dice)

	dice_rolls = simulateDiceRolls(dice)
	probability = calculateProbabilty(dice_rolls) 
	printResults(probability)
  
