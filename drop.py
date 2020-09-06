import unicornhat as uh
import time
import random

uh.set_layout(uh.HAT)
uh.brightness(1)

while True:
	for x in range(8):
		for y in range(8):
			uh.set_pixel(x,y,255,215,0)
		uh.show()
		time.sleep(0.3)
	uh.clear()
	uh.show()


