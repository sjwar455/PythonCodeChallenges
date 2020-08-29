##############################################################################################
# File: sortWords.py    
# Author: Sam Wareing
# Description: waiting game - user must hit enter as close to the specified time as possible
#
# Input: none                                         
#
# Output: time at which enter was pressed                                          
#
#
##############################################################################################
import sys
import random
import time

if __name__ == "__main__":
    timer = random.randint(2,4)
    userInput = input("Timer is " + str(timer) + " seconds. Press enter to start.")

    if userInput == "":
        stopTimer = "waiting" 
        t0 = time.time()
        while stopTimer != "": stopTimer = input("Press enter at exactly when " + str(timer) + " seconds have elapsed") 
        t1 = time.time()
        result = t1 - t0
        print(result)
