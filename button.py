import RPi.GPIO as GPIO
import time
import sys
import signal 

# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM) 
#GPIO.setmode(GPIO.BOARD)

# This is the GPIO pin number we have one of the door sensor
# wires attached to, the other should be attached to a ground pin.DOOR_SENSOR_PIN = 18
# These are the GPIO pin numbers we have the lights attached to

# Initially we don't know if the door sensor is open or closed...
isOpen = None
oldIsOpen = None 

# Set up the door sensor pin.
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

# Set the cleanup handler for when user hits Ctrl-C to exit
while True: 
    oldIsOpen = isOpen 
    isOpen = GPIO.input(4)
    print ("isOpen %d" % isOpen)
    if (isOpen and (isOpen != oldIsOpen)):  
        print "Space is unoccupied!"  
    elif (isOpen != oldIsOpen):  
        print "Space is occupied!"  
    time.sleep(0.1)
