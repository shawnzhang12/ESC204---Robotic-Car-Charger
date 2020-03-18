import RPi.GPIO as gpio
import time
from time import sleep
from picamera import PiCamera
camera = PiCamera()

camera.start_preview()
#will be "while camera not centered perfectly" for actual use
for i in range(3):
    sleep(3)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    ### Perform operations here
camera.stop_preview()