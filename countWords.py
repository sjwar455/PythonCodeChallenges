##############################################################################################
#
#
##############################################################################################
import sys
import re
from collections import Counter

def countWords(filePath): 
	# find all words with letters, numbers, hyphens, and/or apostrophes 
	words = re.findall(r"\w+|[']\w+|\w+[']|\w+['-]*\w+", open(filePath).read().lower())
	print("\nTotal unique words:\t", len(words))	
	print("\nWORD\tCOUNT")
	for word in Counter(words).most_common(20):
		print("{}\t{:d}".format(word[0], word[1]))

def usage(): 
    print("usage: countWords.py /path/to/text/file")

if __name__ == "__main__":
	if len(sys.argv) < 2: 
		usage()
		exit()

	countWords(sys.argv[1])

  
