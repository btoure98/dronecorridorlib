#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import cv2

def draw_function(img, Y, hmin, hmax , ymin, ymax, color, thickness) : 
    """ cette fonction permet de tracer une fonction (liste de valeurs) sur une image
    img: image
    Y: liste de valeurs de la fonction
    hmin,max: entiers ( pixel) entre lesquels on veut tracer la fonction sur l image
    color: couleur rgb
    thickness: entier, largeur
    
    """
    for i in range(0,len(Y)-1):
        debut=(i,int(hmax+Y[i]*(hmin-hmax)/255))
        fin=(i+1,int(hmax+Y[i+1]*(hmin-hmax)/255))
        cv2.line(img, debut, fin, color, thickness)
    
   


def values(img, hauteur):
    """cette fontion permet d extraire la valeur des pixels sur une hauteur donnee dans une image, cette hauteur doit etre en pixels
    img: image
    hauteur: entier ( pixel)
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_array=np.asarray(gray_img)
    return img_array[hauteur]


