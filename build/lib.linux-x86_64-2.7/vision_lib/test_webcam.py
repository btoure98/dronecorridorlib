#! /usr/bin/env python2
#import vision_lib
from detection import *
from filtering import *
from draw import *
import numpy as np
import cv2



cap = cv2.VideoCapture(0) # 0 means /dev/video0, 1 for /dev/video1, ...   
test=True
while test :
    #get image flow
    _, img = cap.read()

    # color grey

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    #detect lines, convert and filter them
    lsd_detector= cv2.createLineSegmentDetector()

    lines=(lsd_detector.detect(gray_img)[0])
    if lines is None:
        pass
    else:
        lines=convert(lines)

        lines=longer_than(lines, 50)

        #draw segments and lines
        color=(0,0,255)
        color1=(255, 0, 0)
        thickness=2
        draw_segments(img, lines, color, thickness)
        draw_lines(img, lines, color1, thickness)
    #show image

    #cv2.imshow('img',img)

    #quit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()