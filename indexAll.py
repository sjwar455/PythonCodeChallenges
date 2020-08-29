##############################################################################################
# File: sortWords.py    
# Author: Sam Wareing
# Description: identify all indices of a given number within a multidimensional array       
#              consisting of random lengths and values
#
# Input: number to search for                         
#
# Output: list of indices                                                         
#
#
##############################################################################################
import sys
import random
arr = [[[1, 2, 2,], 2, [1, 3]], [1, 2, 3]]

def indexAll(arr, num): 
    indices = []
    for i in range(len(arr)):
        if arr[i] == num:
            indices.append([i])
        elif isinstance(arr[i], list):
            for n in indexAll(arr[i], num):
                indices.append([i]+n)
    return indices

def usage():
    print("usage: " + sys.argv[0] + " string") 

if __name__ == "__main__":
    # check if an arguement was passed
    if len(sys.argv) < 2: 
        usage()
        exit() 
    num = int(sys.argv[1])
    print(indexAll(arr, num))


