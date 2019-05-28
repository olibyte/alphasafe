#!/usr/bin/python

import sys, os, time
import RPi.GPIO as GPIO

#This code was used during the demo. The code has since been modified for improved fault tolerance.
GPIO.setmode(GPIO.BOARD) #Set GPIO to pin numbering
PIR = 8 #Assign pin 8 to PIR
LED = 10 #Assign pin 10 to LED
GPIO.setup(PIR, GPIO.IN) #Setup GPIO pin PIR as input
GPIO.setup(LED, GPIO.OUT) #Setup GPIO pin for LED as output
print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup
print ("AlphaSafe Active")
print ("Press Ctrl+c to end program")
time.sleep(5)
try:
	while True:
		if GPIO.input(PIR) == True: #If PIR pin goes high, motion is detected
			print ("Motion Detected!")
			GPIO.output(LED, True) #Turn on LED
			time.sleep(3) #Keep LED on for 3 seconds
			os.system("sudo /home/pi/take_pics")
			#os.system("sudo /home/pi/send_email") #remove the '#' sign to include the email notification module
			#os.system("sudo /home/pi/send_sms") #remove the '#' sign to include the sms notification module
			GPIO.output(LED, False) #Turn off LED
			time.sleep(1)
			print("Security alert! Please check the security directory of your AlphaSafe.")
			time.sleep(30)

except KeyboardInterrupt: #Ctrl+c
	pass #do nothing, continue to finally block

finally:
	GPIO.output(LED, False) #Turn off LED
	GPIO.cleanup() #reset all GPIOs
	print ("Program ended")
