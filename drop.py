import unicornhat as uh
import time
import random

uh.set_layout(uh.HAT)
uh.brightness(0.5)

def dropBlock(x, b):
	for y in range(8-b):
		uh.set_pixel(x,y,255,0,0)
		uh.set_pixel(x,y-1,0,0,0)
		uh.show()
		time.sleep(0.1)

def dropColumn(x):
	for b in range(8):
                dropBlock(x, b)

for x in range(8):
	dropColumn(x)
