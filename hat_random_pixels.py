#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
a = 0

while a < 20:
    x = random.randint(0,7)
    y = random.randint(0,7)
    c = random.randint(0,255)
    sense.set_pixel(x,y,(c,0,c))
    time.sleep(.5)
    sense.set_pixel(x,y,(0,0,0))
    time.sleep(.5)
    a+=1

sense.clear()
