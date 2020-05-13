#! /usr/bin/env python2
#import vision_lib
from detection import *
from filtering import *
from draw import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
import vision_lib
from std_msgs.msg import String,Int32,Int32MultiArray,MultiArrayLayout,MultiArrayDimension

def detect(img, time):
    """ detecter les lignes et le point de fuite puis 
    img: image
    time=temps
    voir exemple 3"""
    gray_img  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detection de lignes
    lsd_detector = cv2.createLineSegmentDetector()
    lines = (lsd_detector.detect(gray_img)[0])
    
    if lines is None:
        pass
    else:
        #detecter le point de fuite 
        lines = convert(lines)
        lines = longer_than(lines, 70)
        lines = list(lines)
        lines = [line for line in lines if abs(line[5])>0.2 ]
        lines = [line for line in lines if abs(line[4])>0.4 ]
        lines = np.array(lines)
        color = (0,0,255)
        color1 = (255, 0, 0)
        thickness = 1
        thickness1 = 2
        vanish_point = vision_lib.vanishing_point.vanishing_point(lines,img)
        vp = vanish_point

        #chercher les lignes au sol a gauche et a droite et notamment les plus proches du point de fuite
        if vanish_point is not None:
            cv2.circle(img,vanish_point,5, color)
            lines_left=[line for line in lines if line[4]<0 ]
            lines_right=[line for line in lines if line[4]>0 ]
            distances_right_to_vp=[vp[0]*line[4]+vp[1]*line[5]+line[6] for line in lines_right]
            distances_left_to_vp=[vp[0]*line[4]+vp[1]*line[5]+line[6] for line in lines_left]
            line_left,line_right=[],[]
            if len(lines_left)>0:    
                line_left=max(zip(distances_left_to_vp, lines_left))[1]
            if len(lines_right)>0:
                line_right=max(zip(distances_right_to_vp, lines_right))[1]
        else:
            return   
        #dessiner les lignes et renvoyer les poitns de fuite
        draw_segments(img, lines, color, thickness1)
        draw_lines(img, lines, color1, thickness)
        return (vanish_point, [line_right,line_left])


        


