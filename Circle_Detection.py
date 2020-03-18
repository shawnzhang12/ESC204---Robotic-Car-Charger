
import cv2

img = cv2.imread('image7.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 3, 3)
retval, threshold = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
cv2.imwrite("image7_binarized.jpg",threshold)
circles = cv2.HoughCircles(threshold, cv2.HOUGH_GRADIENT, 1, 200, param1=100, param2=15, minRadius=10, maxRadius=200)
print(circles)
for i in circles[0]:
    cv2.rectangle(img,(round(i[0]-i[2]),round(i[1]+i[2])),(round(i[0]+i[2]),round(i[1]-i[2])),(0,0,255),2)
cv2.imwrite("image7_port_detection.jpg",img)

