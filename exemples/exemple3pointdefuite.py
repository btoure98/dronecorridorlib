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
    time=0
    

    
    #trouver et tracer le point de fuite
    vision_lib.linedetector.detect(img, time)
    
        
    #montrer image
    cv2.imshow('img',img)

    #quit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()