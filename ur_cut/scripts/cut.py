#!/usr/bin/env python

import cv2
import roslib
import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Vector3


def cut():
    rospy.loginfo('Package found: Start Cutting!')
    # start cutting    

def packageFound():
    # compair PointStamp values with defined ones (tollerance)
    # if true return True
    return False

def callback(msg):
    x = msg.point.x
    y = msg.point.y
    z = msg.point.z
    #rospy.loginfo('x: {}, y: {}, z: {}'.format(x, y, z))
    if packageFound():
        cut()

#rostopic type /object_recognition/position_midpoint 
#geometry_msgs/PointStamped
def main():
    rospy.init_node('packet_cut') # ,anonymous=True, disable_signals=True
    rospy.Subscriber("/object_recognition/position_midpoint", PointStamped, callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()