#!/usr/bin/env python3
########################################################################
# Filename    : ColorfulLED.py
# Description : Random color change ColorfulLED
# Author      : aytha@gmail.com
# modification: 2021/01/23
########################################################################
from gpiozero import RGBLED
import time
import random

pins = [17, 18, 27]         # define the BCM pins for R:17,G:18,B:27 

def setup():
    global rgb_led
    rgb_led = RGBLED(*pins, active_high=False)


def loop():
    while True :
        r=random.random()  #get a random in (0.0,1.0)
        g=random.random()
        b=random.random()
        rgb_led.color = (r,g,b)          #set random as a duty cycle value 
        print ('r=%d, g=%d, b=%d ' %(r * 100 ,g * 100, b * 100))
        time.sleep(2)
        

    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    loop()
