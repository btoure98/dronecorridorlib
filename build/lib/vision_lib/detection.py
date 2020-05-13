import math
import numpy as np

def racine (x0,y0,x1,y1) :
    """cette fonction fonction calcule le b de l equation a*x+b*y+c=0 quand on lui donne deux points de la droite
    x0, y0 sont les coordonnees du premier point et x1, y0 celles du second"""
    return 1/math.sqrt(1+((y0-y1)/(x0-x1))**2)

def convert(segments):
    """cette fonction convertit une array contenant des segments dans ses lignes en array contenant des lignes c est a dire 
    les deux points et les coeffs de la droite passant par les deux points
    segments : nx4 numpy array """
    segments_conv=[]
    for segment in segments:
        x0,y0,x1,y1=segment[0][0],segment[0][1],segment[0][2],segment[0][3]
        #calculer b
        b= racine(x0, y0, x1 , y1)
        #calculer a
        if (y0-y1)/(x0-x1)<0:
            
            a=math.sqrt(1-b**2)
        else:
            a=-math.sqrt(1-b**2)
        #calculer c et la distance entre le deux points
        c = -a*x1 -b*y1
        n = math.sqrt((x1-x0)**2 + (y1-y0)**2)
        segments_conv.append([x0,y0,x1,y1,a,b,c,n])
    
    return np.array(segments_conv)


	