##############################################################################################
#
#
##############################################################################################
import sys
import re
from collections import Counter

def countWords(filePath): 
	words = re.findall(r"[0-9a-zA-Z-']+", open(filePath, encoding='utf-8').read().upper())

	# write results to a file
	file = open('countWordsResult.txt', 'w')
	lines = "\nTotal words:\t{:d}\nWORD\tCOUNT".format(len(words))
	file.write(lines)

	for word in Counter(words).most_common(20):
		line = "\n{}\t{:d}".format(word[0], word[1])
		file.write(line)

	with open('countWordsResult.txt', 'r') as file: 
		print(file.read())

def usage(): 
    print("usage: countWords.py /path/to/text/file")

if __name__ == "__main__":
	if len(sys.argv) < 2: 
		usage()
		exit()

	countWords(sys.argv[1])

  
