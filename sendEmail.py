##############################################################################################
# File: sendEmail.py    
# Author: Sam Wareing
# Description: send an email             
#
# Input: user email and password
#
# Output: none
#
#
##############################################################################################
import smtplib
from getpass import getpass

if __name__ == "__main__":  
    sender = input('username: ')
    password = getpass('Password:')
    print(sender)
    print(password)


