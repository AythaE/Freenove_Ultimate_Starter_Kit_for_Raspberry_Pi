#!/usr/bin/env python3
########################################################################
# Filename    : BreathingLED2.py
# Description : Breathing LED
# Author      : aythae@gmail.com
# modification: 2021/01/23
########################################################################
from gpiozero import PWMLED
import time

LedPin = 18     # define the LedPin

def setup():
    global p

    p = PWMLED(LedPin, frequency=100)      # set PWM Frequence to 500Hz

def loop():
    p.pulse(fade_in_time=2, fade_out_time=2, background=False)
        


if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    
    loop()

