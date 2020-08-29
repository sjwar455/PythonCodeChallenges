##############################################################################################
# File: sortWords.py    
# Author: Sam Wareing
# Description: sorts a string of words alphabetically 
#
# Input: String of words separated by a single space  
#
# Output: String of same words sorted alphabetically                               
#
#
##############################################################################################
import sys

def usage():
    print("usage: " + sys.argv[0] + " string") 

if __name__ == "__main__":
    # check if an arguement was passed
    if len(sys.argv) < 2: 
        usage()
        exit() 

    words = sys.argv[1]
    result = ' '.join(sorted(words.split(' '), key=str.lower))    
    print(result)

