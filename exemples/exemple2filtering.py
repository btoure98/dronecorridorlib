#! /usr/bin/env python2
#import vision_lib
import vision_lib
import numpy as np
import cv2


#dire qu on veut la video de la webcam
cap = cv2.VideoCapture(0) # 0 means /dev/video0, 1 for /dev/video1, ...   
test=True
while test :
    #capturer la video 
    _, img = cap.read()

    # colorer en gris

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    #detecter les segments dans l image, les convertir et les filtrer
    lsd_detector= cv2.createLineSegmentDetector()
    lines=(lsd_detector.detect(gray_img)[0])
    if lines is None:
        pass
    else:
        lines=vision_lib.detection.convert(lines)

        lines=vision_lib.filtering.longer_than(lines, 50)

        #draw segments and lines
        color=(0,0,255)
        color1=(255, 0, 0)
        thickness=2
        vision_lib.draw.draw_segments(img, lines, color, thickness)
        vision_lib.draw.draw_lines(img, lines, color1, thickness)
        
    #montrer image
    cv2.imshow('img',img)

    #quit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()