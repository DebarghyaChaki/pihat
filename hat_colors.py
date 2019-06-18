#!/usr/bin/env python
# this script will defne colors for a scrolling message on the piHAT
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors
red = (255,0,0)
blue = (0,0,255)

speed = 0.05

message = "NO U *2"

sense.show_message(message,speed,text_colour=blue, back_colour=red)

sense.clear()
