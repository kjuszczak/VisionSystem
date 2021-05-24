# import the necessary packages
import cv2
import numpy as np


class ColorDescriptor:

    def describe(self, chan, eps=1e-7):
        hist = np.array(cv2.calcHist([chan], [0], None, [256], [0, 256]))
        norm = np.linalg.norm(hist)
        normal_array = hist / norm
        # find the peak pixel values for R, G, and B
        # [np.std(normal_array), np.argmax(normal_array) / len(normal_array)]
        return [np.std(normal_array), np.argmax(normal_array) / len(normal_array)]
