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

def get_prime_factors(number):
    prime_factorization = []
    print(str(number)) 

    return prime_factorization
def usage():
    print("usage: " + sys.argv[0] + " integer") 

if __name__ == "__main__":
    if len(sys.argv) < 2: 
        usage()
        exit() 
    try: 
        number = int(sys.argv[1])
    except: 
        usage()
        exit()

    print(get_prime_factors(number)) 
