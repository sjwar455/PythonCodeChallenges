##############################################################################################
# File: diceSim.py      
# Author: Sam Wareing
# Description: script to determine probability of dice rolls using monte carlo simulation
#
#
#
##############################################################################################
import sys
from random import randint
from collections import Counter

def simulateDiceRolls(dice, num_simulations):
	counts = Counter()
	for roll in range(num_simulations):
		counts[sum((randint(1, sides) for sides in dice))] += 1

	print("\nOUTCOME\tPROBABILITY")
	for outcome in range(len(dice), sum(dice)+1): 
		print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_simulations))


def usage(): 
    print("diceSim.py # # #....")

if __name__ == "__main__":
	print("let's sim some dice") 

	if len(sys.argv) < 2: 
		usage()
		exit()

	num_simulations = input("How many simulations? press enter for default 1000000 ")
	
	if num_simulations == "": 
		num_simulations = 1000000
	else:
		num_simulations = int(num_simulations)

	n = len(sys.argv)
	dice = [int(sys.argv[i]) for i in range(1, n)]

	simulateDiceRolls(dice, num_simulations)


  
