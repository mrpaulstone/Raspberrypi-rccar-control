#!/usr/bin/env python

from gpiozero import Motor, Servo
import RPi.GPIO as GPIO
from time import sleep
from evdev import InputDevice, categorize, ecodes

# Setup pins for the motors
motor = Motor(20, 21)


myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000

servo = Servo(18,min_pulse_width=minPW,max_pulse_width=maxPW)

# servo.min()
# sleep(1)
# servo.max()
# sleep(1)

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    #filters by event type
    if event.type == ecodes.EV_ABS:
       # print(event)
       # The section below works out the left / right position of the servo for steering
        if event.code == 00:
                print("00")
                print(event)
                if event.value < 65535:
                        lrcalc = event.value / 65535.0
                        lrcalcc = round(lrcalc,1)
                        print("lrcalcc = ", lrcalcc)
                        lrcalcx2 = lrcalcc * 2
                        print ("lrcalcx2 = ", lrcalcx2)
                        lrcalc2xm1 = lrcalcx2 - 1
                        print ("lrcalcx2m1 = ", lrcalc2xm1)
                        print("Full Left")
                        mannacalc = lrcalcc - (1-lrcalcc)
                        print("Mannacalc =", mannacalc)
                        servo.value=lrcalc2xm1
        if event.code == 01:
                print("01")
                print(event)
        if event.code == 02:
                print("02")
                print(event)

        if event.code == 9:
                # this is for controlling the forward movement
                print("09 - right trigger")
                print(event.value)
                if event.value > 1:
                        print("ON")
                        speedcalc = event.value / 1023.0
                        speedclean = round(speedcalc, 4)
                        print("speedclean ", speedclean) 
                        motor.forward(speed=speedclean)
                        sleep(0.0001)
                if event.value < 1:
                        print("OFF")
                        motor.stop()
                        # servo.min()
                        sleep(0.0001)
                        # led.off()






