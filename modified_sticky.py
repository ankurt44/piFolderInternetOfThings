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
UP_PIXELS = [[3, 0], [4, 0]]
DOWN_PIXELS = [[3, 7], [4, 7]]
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
CENTRE_PIXELS = [[3, 3], [4, 3], [3, 4], [4, 4]]
PIXELS = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3]]#,[2,0],[2,1],[2,2],[2,3]]

def set_pixels(pixels, col):
    for p in pixels:
        sense.set_pixel(p[0], p[1], col[0], col[1], col[2])


def handle_code(code, colour):	
    fp = open('parkingSpotStatus.csv','w')
    if code == ecodes.KEY_DOWN:
	print 'free'
	fp.write('FREE')
	sense.show_message('FREE',text_colour=RED,back_colour=GREEN)
    elif code == ecodes.KEY_UP:
	print 'occupied'
	fp.write('OCCUPIED')
	sense.show_message('OCCUPIED',text_colour=GREEN,back_colour=RED)
    fp.close()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]

try:
    sense.show_message("",back_colour=[0,255,0])
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
		#write code to check if its not FREE.. then dont check for UP and DOWN joystick
        	handle_code(event.code, WHITE)
except KeyboardInterrupt:
    sys.exit()
