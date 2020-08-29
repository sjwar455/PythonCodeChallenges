##############################################################################################
# File: isPalindrome.py    
# Author: Sam Wareing
# Description: determines if a string is a palindrome, considering only A-Z characters
#
# Input: String  
#
# Output: Boolean                               
#
#
##############################################################################################
import sys
import re


def isPalindrome(string): 
    # use regular expression to remove all non-alpha characters
    regex = re.compile('[^a-zA-Z]')     # a character not equal to a-z and A-Z
    string = regex.sub('', string)      # substitute anything matching regex in string 
    string = string.lower()             # make string all lowercase 

    # invert string
    invStr = string[::-1]

    # return comparison
    return invStr == string


def usage():
    print("usage: " + sys.argv[0] + " string") 

if __name__ == "__main__":
    # check if an arguement was passed
    if len(sys.argv) < 2: 
        usage()
        exit() 
    
    print(isPalindrome(sys.argv[1]))

