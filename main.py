#!/usr/bin/python

import sys
import os
import time
import RPi.GPIO as GPIO

#This code has been modified to include an extra sensor, thereby decreasing the likelihood of recording false positives.
GPIO.setmode(GPIO.BOARD)  # Set GPIO to pin numbering

PIRA = 8  # Assign pin 8 to PIRA
PIRB = 12  # Assign pin 12 to PIRB
LED = 10  # Assign pin 10 to LED
GPIO.setup(PIRA, GPIO.IN)
GPIO.setup(PIRB, GPIO.IN)
# Setup GPIO pin PIR as input
GPIO.setup(LED, GPIO.OUT)  # Setup GPIO pin for LED as output
print("Sensor initializing . . .")
time.sleep(3)  # 3 seconds for sensors to initialise
print("Active")
print("Press Ctrl+C to end program")
while True:
    try:
        if (((not PIRA) or (not PIRB)):
            # If both sensors detect no motion, LED will flash intermittently every 3 seconds.
            GPIO.output(LED, True)  # Turn on LED
            time.sleep(1)  # Keep LED on for 1 seconds
            GPIO.output(LED, False)  # Turn off LED
            time.sleep(3)
        else:
            # Both sensors have detected motion, alarm is to be triggered.
            print("Motion detected!")
            GPIO.output(LED, True)  # Turn on LED
            os.system("sudo /home/pi/take_pics") #take 5 photos of intruder
            os.system("sudo /home/pi/send_sms") #include this to receive sms alert
            os.system("sudo /home/pi/send_email") #include this to receive email alert
            time.sleep(5) #Wait 30 seconds before rechecking for room occupancy

    except KeyboardInterrupt:  # Ctrl+c
        pass  # Do nothing, continue to finally block

    finally:
        GPIO.output(LED, False)  # Turn off LED in case left on
        GPIO.cleanup()  # reset all GPIO
        print("Program ended")