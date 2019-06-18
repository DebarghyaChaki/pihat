#!/usr/bin/env python
#this script will show a matrix of colors on the piHAT
from sense_hat import SenseHat
import time
sense = SenseHat()
r = (255,0,0)
b = (0,0,255)
w = (255,255,255)

pixels = [
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w, 
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w,
]

sense.set_pixels(pixels)
time.sleep(10)

sense.clear()
