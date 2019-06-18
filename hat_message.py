#!/usr/bin/env python
#this script will show a scrolling message on the pi HAT
from sense_hat import SenseHat
sense = SenseHat()

#send the text Hi to the show_message() function
sense.show_message("Hi")
