#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import CompressedImage

import vision_lib.linedetector


class Test:
    
    def __init__(self):
        self.sub = rospy.Subscriber("/image_in/compressed",  CompressedImage, self.on_image,  queue_size = 1, buff_size=2**22)
        self.pub=rospy.Publisher("/opticalflow",CompressedImage, queue_size=1)
    def on_image(self, msg):
        compressed_in = np.fromstring(msg.data, np.uint8)
        frame         = cv2.imdecode(compressed_in, cv2.IMREAD_COLOR)

        # if time is required in your cumputation, consider the current time
        # as the one recorded in the message timestamps. This enables a coherent
        # time sequence when the images come from a ros bag, since ros bag execution
        # can be paused, run step by step, ...
        now = msg.header.stamp
        print(vision_lib.optical_flow.values(frame,300))
        
        
        
        cv2.imshow('img',frame)
        cv2.waitKey(2)
        
        new_msg = CompressedImage()
        new_msg.header.stamp = rospy.Time.now()
        new_msg.format = "jpeg"
        new_msg.data = np.array(cv2.imencode('.jpg', frame)[1]).tostring()

        # Publish new image
        self.pub.publish(new_msg)


if __name__ == '__main__':
    rospy.init_node('test')
    test = Test()
    rospy.spin()