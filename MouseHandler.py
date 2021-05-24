# import the necessary packages

import cv2


refPt = []
cropping = False
img = None

def click_and_crop(event, x, y, flags, param):

    global refPt, cropping, img

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("img", img)