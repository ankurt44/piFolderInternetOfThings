#!/usr/bin/python
import sys
import time
from sense_hat import SenseHat
from evdev import InputDevice, list_devices, ecodes

print("Press Ctrl-C to quit")
time.sleep(1)

sense = SenseHat()
sense.clear()  # Blank the LED matrix

found = False;
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == 'Raspberry Pi Sense HAT Joystick':
        found = True;
        break

if not(found):
    print('Raspberry Pi Sense HAT Joystick not found. Aborting ...')
    sys.exit()

# 0, 0 = Top left
# 7, 7 = Bottom right
PIXELS = [[0,0],[0,1],[0,2],[1,0],[1,2],[1,1]]# [7,7]]

def set_pixels(pixels, col):
    for p in pixels:
        sense.set_pixel(p[0], p[1], col[0], col[1], col[2])


BLUE = [0, 0, 255]

try:
    fread = open('parkingSpotStatus.csv','w')
    #text = fread.read()
    fread.write('RESERVED')
    #text = text.split()[0]
    #if(text == 'RESERVED'):
    sense.show_message('RESERVED',back_colour = BLUE, text_colour=[255,0,0])
 
except KeyboardInterrupt:
    sys.exit()
