
import cv2
import RPi.GPIO as gpio
import time
from time import sleep
from picamera import PiCamera

'''
camera = PiCamera()

camera.start_preview()
for i in range(3):
    sleep(3)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)

camera.stop_preview()
#Example code for detecting port in one image
img = cv2.imread('image1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 4, 4)
retval, threshold = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
cv2.imwrite("img1_binarization.png",threshold)
circles = cv2.HoughCircles(threshold, cv2.HOUGH_GRADIENT, 1, 200, param1=10, param2=10, minRadius=10, maxRadius=300)
#print(circles)
#print(circles[0][0][1])
for i in circles[0]:
    cv2.rectangle(img,(round(i[0]-i[2]),round(i[1]+i[2])),(round(i[0]+i[2]),round(i[1]-i[2])),(0,0,255),2)
cv2.imwrite("img1_holes.png",img)'''


gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(23, gpio.OUT) #GPIO23 = Direction for stepper motor 0
gpio.setup(24, gpio.OUT) #GPIO24 = Step for stepper motor 0

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
