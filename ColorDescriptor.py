# import the necessary packages
import cv2
import numpy as np


class ColorDescriptor:

    def describe(self, chan):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        # find the peak pixel values for R, G, and B
        return np.argmax(hist)
