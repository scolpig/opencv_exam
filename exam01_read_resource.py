import cv2

# img = cv2.imread('./resources/lena.png')
#
# cv2.imshow('Lena Soderberg', img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture('./resources/test_video.mp4')
#
# while cv2.waitKey(33) != ord('q'):
#     _, img = cap.read()
#     img = cv2.resize(img, (640, 480))
#     cv2.imshow('test video', img)

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
while cv2.waitKey(33) != ord('q'):
    _, img = cap.read()
    # img = cv2.resize(img, (640, 480))
    cv2.imshow('test video', img)


