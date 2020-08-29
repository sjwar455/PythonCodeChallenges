##############################################################################################
# File: getPrimeFactors.py 
# Author: Sam Wareing
# Description: finds the prime factorization for the input number
#
# Input: integer 
#
# Output: array containing the prime factors 
#
#
##############################################################################################
import sys

def getPrimeFactors(N):
    factors = []
    divisor = 2     # start with smallest prime number, 2
    
    while divisor <= N:                 # repeat loop until all prime factors are found
        if N % divisor == 0:            # check if number is evenly divided by divisor
            factors.append(divisor)     # add prime factor to list
            N = N/divisor               # use the quotient as the new number to factor
        else:
            divisor+=1                  # if divisor does not evenly divide, incremente by 1

    return factors

def usage():
    print("usage: " + sys.argv[0] + " int") 

if __name__ == "__main__":
    # check if an arguement was passed
    if len(sys.argv) < 2: 
        usage()
        exit() 

    # check if the arguement passed is an int
    try: 
        number = int(sys.argv[1])
    except: 
        usage()
        exit()

    # Find the prime factorization for the passed in number
    factors = getPrimeFactors(number)

    # print results
    print(factors) 


