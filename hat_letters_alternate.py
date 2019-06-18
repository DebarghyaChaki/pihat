#!/usr/bin/env python
# displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.show_letter("H", (0,255,0))
time.sleep(1)
sense.show_letter("I", (0,255,255))
time.sleep(1)
sense.show_letter("?", (255,0,125))
time.sleep(1)
sense.clear()
