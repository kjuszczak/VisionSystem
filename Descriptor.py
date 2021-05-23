# import the necessary packages
import cv2
import numpy as np

from LocalBinaryPatterns import LocalBinaryPatterns
from ColorDescriptor import ColorDescriptor

class Descriptor:
    def __init__(self, lbpDescriptor):
        # store the number of points and radius
        self.lpbDescriptor = LocalBinaryPatterns(lbpDescriptor[0], lbpDescriptor[1])
        self.colorDescrptor = ColorDescriptor()

    def describe(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = self.lpbDescriptor.describe(gray)

        chans = cv2.split(image)
        res = []
        for chan in chans:
            res.append(self.colorDescrptor.describe(chan))

        return np.concatenate((res, hist))
