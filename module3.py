##############################################
# File Name: module3.py
# Version: 1.0
# 
# Date: 22 Jyn 17
##############################################

import RPi.GPIO as GPIO
import time
import sys, tty, termios

print '\nModule 3 - watch the LED...\n'

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

ledOnTime = 5

# Turn on LED
print 'Turn the LED on'
GPIO.output(7, True)
time.sleep(ledOnTime)
print 'Turn the LED off'
GPIO.output(7, False)

GPIO.cleanup()
   
print "\nEnd of program"
