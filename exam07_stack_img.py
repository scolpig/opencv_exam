import cv2
import numpy as np



def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
                imgArray[x][y] = cv2.resize(imgArray[x][y],
                                            (0, 0), None, scale, scale)
    hor = []
    for x in range(rows):
        hor.append(np.hstack(imgArray[x]))
    ver = np.vstack(hor)
    return ver
kernel = np.ones((5, 5), np.uint8)
img = cv2.imread('resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgColor = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgEroded = cv2.erode(img, kernel, iterations=1)
imgDialation = cv2.dilate(imgEroded, kernel, iterations=1)

imgStack = stackImages(0.5, [[img, imgGray, imgBlur],
                             [imgCanny, imgEroded, imgDialation]])

cv2.imshow('Image Stack', imgStack)
cv2.waitKey(0)



