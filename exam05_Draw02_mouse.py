import cv2
import numpy as np

def mouse_event(event, x, y, flags, img):
    global center_pos, radius, draw_flag

    new_img = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        draw_flag = True
        center_pos = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw_flag:
            # cv2.circle(new_img, center_pos,
            #            int(((center_pos[0] - x)**2 + (center_pos[1] - y)**2)**0.5),
            #            (200, 100, 100), 2)
            cv2.rectangle(new_img, center_pos, (x, y), (50, 50, 200), 2)
            cv2.imshow('Image', new_img)
    elif event == cv2.EVENT_LBUTTONUP:
        draw_flag = False
        # cv2.circle(img, center_pos,
        #            int(((center_pos[0] - x)**2 + (center_pos[1] - y)**2)**0.5),
        #            (200, 100, 100), 2)
        cv2.rectangle(img, center_pos, (x, y), (50, 50, 200), 2)
        cv2.imshow('Image', img)

draw_flag = False
center_pos = (0, 0)
radius = 3
img = np.full((500, 500, 3), 255, dtype=np.uint8)

cv2.imshow('Image', img)
cv2.setMouseCallback('Image', mouse_event, img)
cv2.waitKey(0)

