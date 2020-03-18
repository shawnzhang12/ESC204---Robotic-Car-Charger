import RPi.GPIO as gpio
import time
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(23, gpio.OUT) #GPIO23 = Direction for motor 0
gpio.setup(24, gpio.OUT) #GPIO24 = Step for motor 0

gpio.output(23, True)
StepCounter = 0
# waittime controls speed
WaitTime = 0.005

# Start main loop
while StepCounter < 200:
    # turning the gpio on and off tells the easy driver to take one step
    gpio.output(24, True)
    time.sleep(WaitTime)
    gpio.output(24, False)
    time.sleep(WaitTime)
    StepCounter += 1
gpio.cleanup()