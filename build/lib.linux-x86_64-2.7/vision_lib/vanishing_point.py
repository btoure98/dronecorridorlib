#! /usr/bin/env python
# -*- coding: utf-8 -*-
from filtering import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import CompressedImage
import sys

def sci(values, confidence) :
    nb=values.shape[0]
    values=np.sort(values)
    size=(int)(nb*confidence+.5)
    nb_iter=nb - size + 1
    sci=None
    sci_width =sys.float_info.max
    inf=0
    sup=size
    for i in range(nb_iter) :
        sciw = values[sup-1] - values[inf]
        if sciw < sci_width :
            sci       = values[inf:sup]
            sci_width = sciw
        inf += 1
        sup += 1
    return sci

def vanishing_point(lines,img):
    h, w = img.shape[0], img.shape[1]
    intersections=intersect(lines)
    intersections=list(intersections)
    intersections=[point for point in intersections if (0<point[0]<w and 0<point[1]<h)]
    
    #print(len(intersections))
    intersections=np.array(intersections)
    #print(intersections)
    if len(intersections)>0 or intersections==np.array([]):
        return (int(np.mean(sci(intersections[:,0], 0.7))),int(np.mean(sci(intersections[:,1], 0.7))))
    else:
        return None

