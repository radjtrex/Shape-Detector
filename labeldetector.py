# noinspection PyUnresolvedReferences
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import odd as odd
import os
import glob
import imutils


# from PIL import Image
# Rory Spralls
# CSCE 4240
# label class

class LabelDetector:
    def __init__(self):
        pass

    def detect(self, c):
        # initialize the shape name and approximate the contour
        shape = "STOP"
        peri = cv2.arcLength (c, True)
        approx = cv2.approxPolyDP (c, 0.04 * peri, True)
        #print('approx', len(approx))
        # if the shape is a triangle, it will have 3 vertices
        if len (approx) == 3:
                shape = "Triangle"

        # if the shape has 4 vertices, it is either a square or
        # a rectangle
        elif len (approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect (approx)
            area = w / float (h)

            #print ('Area', area)
            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            if .91 < area <= 1.00:
                shape = 'Square'
            elif .80 < area < .87:
                shape = "Triangle"
            elif .70 <= area <= 1.5:
                shape = "Ellipse"
            else:
                shape = "Circle"
            #print('Area', area)
            #if .91 < area <= .95:
               # shape = "Square"
        # if the shape is a pentagon, it will have 5 vertices
        elif len (approx) == 5:
            shape = "Pentagon"

        elif len (approx) == 8 or len(approx) == 6:
            shape = "Circle"

        #elif len (approx) >= 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            #(x, y, w, h) = cv2.boundingRect (approx)
            #are = w / float (h)

           # a square will have an aspect ratio that is approximately
           # equal to one, otherwise, the shape is a rectangle
            #if are < .90:
               # shape = 'ellipse'

        # otherwise, we assume the shape is a circle
        else:
            shape = "STOP"

        # return the name of the shape
        return shape
