##############################################################################################
# File: sendEmail.py    
# Author: Sam Wareing
# Description: send an email             
#
# Input: none
#
# Output: none
#
# Note: sender email might need to be configured to allow less secure apps access
#
#
##############################################################################################
import smtplib
from getpass import getpass

def sendEmail(recipient, subject, body, sender, password):
    # format email
    message = 'Subject: {}\n\n{}'.format(subject, body)

    # send email using the smtplib library
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: 
        server.login(sender, password)                          # login using user credentials
        server.sendmail(sender, recipient, message)            # send email

if __name__ == "__main__":  
    # prompt for email info
    recipient = input('recipient: ')
    subject = input('subject: ') 
    body = input('body: \n')
    sender = input('sender: ')
    password = getpass('password:')     # ensure password is hidden
    
    # send email
    sendEmail(recipient, subject, body, sender, password)
