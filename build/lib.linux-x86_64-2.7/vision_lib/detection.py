import math
import numpy as np

def racine (x0,y0,x1,y1) :
    return 1/math.sqrt(1+((y0-y1)/(x0-x1))**2)

def convert(segments):
    segments_conv=[]
    for segment in segments:
        x0,y0,x1,y1=segment[0][0],segment[0][1],segment[0][2],segment[0][3]
        #print x0
        b= racine(x0, y0, x1 , y1)
        if (y0-y1)/(x0-x1)<0:
            a=math.sqrt(1-b**2)
        else:
            a=-math.sqrt(1-b**2)
        c = -a*x1 -b*y1
        n = math.sqrt((x1-x0)**2 + (y1-y0)**2)
        segments_conv.append([x0,y0,x1,y1,a,b,c,n])
    
    return np.array(segments_conv)


	