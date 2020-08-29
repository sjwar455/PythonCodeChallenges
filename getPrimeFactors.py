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

def getPrimeFactors(number):
    primeFactorization = []

    print("finding prime factorization for " + str(number)) 

    if isPrime(number): 
        print(str(number) + " is prime") 
    else:
        print(str(number) + " is not prime") 
    

    return primeFactorization

def isPrime(n):
    # if the passed number is greater than 1 and is a whole number 
    # check if the number can be evenly divided by a number 2 to n-1 
    # i.e. a number other than 1 and n 
    if n > 1 and n % 1 == 0:
        for i in range(2, n-1):
            if n % i == 0:
                return False

    return True

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

    # print the prime factorization or the passed in int
    print(getPrimeFactors(number)) 
