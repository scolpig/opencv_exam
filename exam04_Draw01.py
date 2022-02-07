import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8) * 255
print(img.shape)

cv2.line(img, (0, 0), (512, 512), (50, 200, 50), 3)
cv2.rectangle(img, (10, 10), (250, 350), (50, 50, 200), 2)
cv2.circle(img, (400, 50), 30, (200, 200, 50), 5)
cv2.ellipse(img, ((150, 150), (200, 100), 10), (200, 50, 50), 2)
cv2.putText(img, 'OPENCV', (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 200, 200), 1)

cv2.imshow('Image', img)

cv2.waitKey(0)







