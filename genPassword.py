##############################################################################################
#
#
##############################################################################################
import sys
from random import randint

wordList = 'diceware.wordlist.asc.txt'

def genPassword(num_words):
	# create dictionary of random short words 
	words = {} 
	for line in open(wordList, 'r').readlines(): 
		(key, val) = line.split()
		words[key] = val 

	# create randomly generated passphrase
	password = ""
	for i in range(1, num_words+1): 
		key = ""
		for k in range(1, 6):
			key += str(randint(1,6)) 
		password += " " + words[key]

	return password[1:]


def usage(): 
    print("usage: genPassword.py num_words")

if __name__ == "__main__":
	if len(sys.argv) < 2: 
		usage()
		exit()

	num_words = int(sys.argv[1])

	print(genPassword(num_words))
  
