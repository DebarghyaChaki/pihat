#!/usr/bin/env python
# displays one letter at a time
from sense_hat import SenseHat
sense = SenseHat()
import time

green = (0,255,0)
cyan = (0,255,255)
raspberry = (255,0,125)

sense.show_letter("H", green)
time.sleep(1)
sense.show_letter("I", cyan)
time.sleep(1)
sense.show_letter("?", raspberry)
time.sleep(1)
sense.clear()
