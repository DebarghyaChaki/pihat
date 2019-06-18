#!/usr/bin/env python
# this script will display letters with random colors on the piHAT
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
#assign a random integer between 0 and 255 to a variable named r
r = random.randint(0,255)

sense.show_letter("N", (r,0,0))
time.sleep(1)
sense.show_letter("O", (0,r,0))
time.sleep(1)
sense.show_letter("2", (0,0,r))
time.sleep(1)

sense.clear()
