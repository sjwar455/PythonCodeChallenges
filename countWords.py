##############################################################################################
#
#
##############################################################################################
import sys
import re
from collections import Counter

def countWords(filePath): 
	# find all words with letters, numbers, hyphens, and/or apostrophes 
	words = re.findall(r"[0-9a-zA-Z-']+", open(filePath, encoding='utf-8').read().upper())
	print("\nTotal words:\t", len(words))	
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

  
