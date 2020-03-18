
import cv2
import RPi.GPIO as gpio
import time
from time import sleep
from picamera import PiCamera
import pynput
from pynput import keyboard
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
##### Stepper Motors #####
gpio.setup(23, gpio.OUT) #gpio23 = Direction for stepper motor 0
gpio.setup(24, gpio.OUT) #gpio24 = Step for stepper motor 0
gpio.setup(8, gpio.OUT) #gpio23 = Direction for stepper motor 1
gpio.setup(7, gpio.OUT) #gpio24 = Step for stepper motor 1
gpio.setup(16, gpio.OUT) #gpio23 = Direction for stepper motor 2
gpio.setup(20, gpio.OUT) #gpio24 = Step for stepper motor 2

#################################################
##########NEED TO ADD INSERTION MOTOR CODE#######
#################################################

StepCounter = 0
WaitTime = 0.005 # waittime controls speed

##### DC Motors (Wheels) #####
enA = 17
in1 = 27
in2 = 22
gpio.setup(enA, gpio.OUT) #gpio17 = ENA for L298N
gpio.setup(in1, gpio.OUT) #gpio27 = IN1 for L298N
gpio.setup(in2, gpio.OUT) #gpio22 = IN2 for L298N
pleft=gpio.PWM(enA,1000)
pleft.start(0)

in3 = 10
in4 = 9
enB = 11

gpio.setup(in3, gpio.OUT) #gpio27 = IN3 for L298N
gpio.setup(in4, gpio.OUT) #gpio22 = IN4 for L298N
gpio.setup(enB, gpio.OUT) #gpio10 = ENB for L298N
pright=gpio.PWM(enB,1000)
pright.start(0)

def on_press(key):
    try:
        #print('Key {0} pressed'.format(key.char))
        ### Code for wasd control of dc motors ###
        if(key.char=='w'):
            print("going forwards")
            gpio.output(in1, gpio.HIGH)
            gpio.output(in2, gpio.LOW)
            gpio.output(in3, gpio.HIGH)
            gpio.output(in4, gpio.LOW)
            pleft.start(100)
            pright.start(100)
        elif(key.char=='s'):
            print("going backwards")
            gpio.output(in1, gpio.LOW)
            gpio.output(in2, gpio.HIGH)
            gpio.output(in3, gpio.LOW)
            gpio.output(in4, gpio.HIGH)
            pleft.start(100)
            pright.start(100)
        elif (key.char == 'a'):
            print("turning left")
            gpio.output(in1, gpio.LOW)
            gpio.output(in2, gpio.HIGH)
            gpio.output(in3, gpio.HIGH)
            gpio.output(in4, gpio.LOW)
            pleft.start(100)
            pright.start(100)
        elif (key.char == 'd'):
            print("turning right")
            gpio.output(in1, gpio.HIGH)
            gpio.output(in2, gpio.LOW)
            gpio.output(in3, gpio.LOW)
            gpio.output(in4, gpio.HIGH)
            pleft.start(100)
            pright.start(100)
        else:
            pleft.start(0)
            pright.start(0)

        ### Code for stepper motors ###
        if (key.char == 'i'): #Moving Up
            gpio.output(8, True)
            gpio.output(16, True)
            gpio.output(7, True)
            gpio.output(20, True)
            time.sleep(WaitTime)
            gpio.output(7, False)
            gpio.output(20, False)
            time.sleep(WaitTime)
        elif (key.char == 'k'): #Moving Down
            gpio.output(8, False)
            gpio.output(16, False)
            gpio.output(7, True)
            gpio.output(20, True)
            time.sleep(WaitTime)
            gpio.output(7, False)
            gpio.output(20, False)
            time.sleep(WaitTime)
        elif (key.char == 'j'): #Moving Left
            gpio.output(24, True)
            gpio.output(23, True)
            time.sleep(WaitTime)
            gpio.output(23, False)
            time.sleep(WaitTime)
        elif (key.char == 'j'): #Moving Right
            gpio.output(24, False)
            gpio.output(23, True)
            time.sleep(WaitTime)
            gpio.output(23, False)
            time.sleep(WaitTime)


    except AttributeError:
        print('Key {0} pressed'.format(key))
        print("Rip")

def on_release(key):
    #print('{0} released'.format(key))
    #Add your code to stop motor
    if (key.char == 'd') or (key.char == 's') or (key.char == 'a') or (key.char == 'w'):
        pleft.start(0)
        pright.start(0)
    if key == keyboard.Key.esc:
        # Stop listener
        # Stop the Robot Code
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
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

'''
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
'''
gpio.cleanup()
