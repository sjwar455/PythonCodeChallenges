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
        exit()
    else:
        while not(isPrime(number)):
            factor = 2                  # start with 2, the smallest prime number
            result = number/factor      # divde the current number by 2

            # if the current number cannot be divided by 2 evenly
            # find the next prime number that it can be evenly divided by
            while result % 1 > 0:       
                factor+=1
                result = number/factor

            primeFactorization.append(factor)   # add the prime factor to the array
            number = result                     # continue the loop to check for remaining prime factors
       
        # add the final prime factor 
        primeFactorization.append(int(number))
    
    return primeFactorization

def isPrime(n):
    # if the passed number is greater than 1 and is a whole number 
    # check if the number can be evenly divided by a number 2 to n-1 
    # i.e. a number other than 1 and n 
    if n > 1 and n % 1 == 0:
        n = int(n)
        for i in range(2, n-1):
            if n % i == 0:
                return False

    return True

def verifyResults(primeFactorization):
    result = 1 
    for i in primeFactorization: 
        result*=i

    return result


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
    primeFactorization = getPrimeFactors(number)

    # verify the prime factorization was correctly calculated
    result = verifyResults(primeFactorization)

    # print results
    print(primeFactorization) 
    print("product of factorization: " + str(result)) 


