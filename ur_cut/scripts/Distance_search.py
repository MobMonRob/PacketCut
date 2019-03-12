#!/usr/bin/env python

import cv2
import roslib
import rospy
import time

from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2




def startCutting():
    rospy.loginfo('Package found: Start Cutting!') 
    #time.sleep(3)
    # TODO aufrufen von cutter

def searchForDistanceIn(point_cloud):
    points_3d = []
    
    midpoint_x = (95,96,97,98,99,100,101,102,103,104)
    midpoint_y = (80,81,82,83,84,85,86,87,88,89)
    
    rospy.loginfo("Get distance from:")
    rospy.loginfo("X: " + str(midpoint_x) + "Y: " + str(midpoint_y))


    for mx in midpoint_x:
        for my in midpoint_y:
            midpoint = (mx, my)
            points_2d = ([midpoint])

            # skip_nans to protect for traceback NaN Error
            for point_3d in list(pc2.read_points(point_cloud, uvs=points_2d, skip_nans=True)):
                x, y, z = point_3d
                return z

    return None
            

def packageInDistance(point_cloud):
    z = searchForDistanceIn(point_cloud)
    if z is not None:
        rospy.loginfo("Distanze to Object: " + str(z))
        if z < 0.15:
            rospy.loginfo("Close Object, is in cutting!")
        elif 0.15 < z < 0.35:
            rospy.loginfo("Packet in Range! Start cutting ...")
            return True

    rospy.loginfo("No Distance in PointCloud")
    return False

def callback(msg):  
    if packageInDistance(msg):
        startCutting()


def main():
    rospy.init_node('packet_cut', anonymous=True, disable_signals=True)
    rospy.Subscriber("/royale_camera_driver/point_cloud", PointCloud2, callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
