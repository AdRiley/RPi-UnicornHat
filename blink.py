import unicornhat as uh
import time
import random

uh.set_layout(uh.HAT)
uh.brightness(1)

while True:
	uh.set_pixel(random.randint(0,7),random.randint(0,7),255,215,0)
	uh.set_pixel(random.randint(0,7),random.randint(0,7),random.randint(0,255),random.randint(0,255),random.randint(0,255))
	uh.show()
	time.sleep(0.3)
	uh.clear()
	uh.show() 
 
