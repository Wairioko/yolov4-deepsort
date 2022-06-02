import os
import cv2
import random
import numpy as np
import tensorflow as tf
import pytesseract
from core.utils import read_class_names
from core.config import cfg

# function to count objects, can return total classes or count per class
def count_objects(data, by_class = False,
 allowed_classes = list(read_class_names(cfg.YOLO.CLASSES).values())):
    boxes, scores, classes, num_objects = data

    #create dictionary to hold count of objects
    counts = dict()

    # if by_class = True then count objects per class
    if by_class:
        class_names = read_class_names(cfg.YOLO.CLASSES)

        # loop through total number of objects found
        for i in range(num_objects):
            # grab class index and convert into corresponding class name
            class_index = int(classes[i])
            class_name = class_names[class_index]
            if class_name in allowed_classes:
                counts[class_name] = counts.get(class_name, 0) + 1
            else:
                continue

    # else count total objects found
    else:
        counts['total object'] = num_objects
    
    return counts

def getSpeed(pointList):
    dx = 0
    dy = 0
    for x in range(len(pointList)-1):
        dx += pointList[bbox[0]+1][0] - pointList[bbox[0]][0]  
        dy += pointList[bbox[0]+1][1] - pointList[bbox[0]][1] 
    speed = math.sqrt(abs(dx * dx - dy * dy))
    return round(speed / 100)
   
