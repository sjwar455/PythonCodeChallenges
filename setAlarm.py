##############################################################################################
# File: setAlarm.py     
# Author: Sam Wareing
# Description: script to set an alarm
#
# Input: Alarm time (seconds), sound file (path), message to display (string)                                         
#
# Output: time at which enter was pressed                                          
#
#
##############################################################################################
import sys
import os
import time

def setAlarm(duration, sound, message): 
    time.sleep(duration)
    os.system("start " + sound) 
    print(message)

def usage(): 
    print("python " + sys.argv[0] + " time sound message")
    print("where time is in seconds, sound is the full path to the sound file, and message is the desired display string") 

if __name__ == "__main__":  
    if len(sys.argv) < 4: 
        usage()
        exit()
    duration = float(sys.argv[1])
    sound = sys.argv[2]
    message = sys.argv[3]
    setAlarm(duration, sound, message)
