import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('./resources/lena.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgEroded = cv2.erode(img, kernel, iterations=1)
imgDialation = cv2.dilate(imgEroded, kernel, iterations=1)

cv2.imshow('Origin image', img)
cv2.imshow('Gray image', imgGray)
cv2.imshow('Blur image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Dialation image', imgDialation)
cv2.imshow('Eroded image', imgEroded)

cv2.waitKey(0)





