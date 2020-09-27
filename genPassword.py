##############################################################################################
#
#
##############################################################################################
import sys
import secrets

wordList = 'diceware.wordlist.asc.txt'

def genPassword(num_words):
	# create list of words
	words_list = [line.split()[1] for line in open(wordList, 'r').readlines()[2:7778]]
	# pick random words from list
	words = [secrets.choice(words_list) for i in range(num_words)]

	# return randomly generated passpharse
	return ' '.join(words)


def usage(): 
    print("usage: genPassword.py num_words")

if __name__ == "__main__":
	if len(sys.argv) < 2: 
		usage()
		exit()

	num_words = int(sys.argv[1])

	print(genPassword(num_words))
  
