#! /usr/bin/env python


import numpy as np
import cv2

def draw_segments(img, lines, color, thickness) :
    for line in list(lines):
        cv2.line(img, (int(line[0]),int(line[1])), (int(line[2]), int(line[3])), color, thickness)


def f(point, line):
    return line[4]*point[0]+ line[5]*point[1]+line[6]


def draw_lines(img, lines, color, thickness) :
    h, w = img.shape[0], img.shape[1]
    coin1, coin2, coin3, coin4= (0,0), (w,0), (w,h), (0,h)
    for line in list(lines):
        bords=[]
        if f(coin1, line)*f(coin2, line)<=1:
            bords.append((int(-line[6]/line[4]),0))
        if f(coin2, line)*f(coin3, line)<=1:
            bords.append((w,int(-(line[6]+w*line[4])/line[5])))
        if f(coin3, line)*f(coin4, line)<=1:
            bords.append((int(-(line[6]+h*line[5])/line[4]),h))
        if f(coin4, line)*f(coin1, line)<=1:
            bords.append((0, int(-line[6]/line[5])))
        if len(bords)==2:
            cv2.line(img, bords[0], bords[1], color, thickness)

    
