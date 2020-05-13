#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import cv2

def draw_function(img, Y, hmin, hmax , ymin, ymax, color, thickness) : 

    for i in range(0,len(Y)-1):
        debut=(i,hmax+Y[i]*(hmin-hmax)/255)
        fin=(i+1,hmax+Y[i+1]*(hmin-hmax)/255)
        cv2.line(img, debut, fin, color, thickness)
    
   
def local_shift(x,Y1,Y2,move, rho, sigma):
    results=[]
    if move=='left':
        shifts=range[1,sigma+1]
    else:
        shifts=range[-sigma,0]
    for shift in shifts:
        diffsignaux=Y1-np.roll(Y2,shift)
        results.append(np.linalg.norm(X[min(x-rho,0):max(x+rho,650)])**2)
    results=zip(results,shifts)
    return min(results)[1]


def values(img, hauteur):
     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     img_array=np.asarray(gray_img)
     return img_array[hauteur]


