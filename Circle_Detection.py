import cv2

img = cv2.imread('carhole.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 0)
retval, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imwrite("blur.png",threshold)
circles = cv2.HoughCircles(threshold, cv2.HOUGH_GRADIENT, 2, 100)
print(circles)
print(circles[0][0][1])
for i in circles[0]:
    cv2.rectangle(img,(round(i[0]-i[2]),round(i[1]+i[2])),(round(i[0]+i[2]),round(i[1]-i[2])),(0,0,255),2)
cv2.imwrite("findcircles.png",img)