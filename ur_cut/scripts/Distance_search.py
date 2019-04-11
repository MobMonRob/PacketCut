#!/usr/bin/env python

import cv2
import roslib
import rospy
import time

from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2


def startCutting():
    rospy.loginfo('Package found: Start Cutting!') 
    #time.sleep(3) # some delay to wait package all the way
    # TODO aufrufen von cutter

def searchForDistanceIn(point_cloud):
    
    # Distance is not searched for all points, only in the middle of the image
    # Create 2D Array with points to search distance for
    midpoint_x = (95,96,97,98,99,100,101,102,103,104)
    midpoint_y = (80,81,82,83,84,85,86,87,88,89)
    
    rospy.loginfo(" ")
    rospy.loginfo("Get distance from:")
    #rospy.loginfo("X: " + str(midpoint_x) + "Y: " + str(midpoint_y))


    for mx in midpoint_x:
        for my in midpoint_y:
            midpoint = (mx, my)
            points_2d = ([midpoint])

            # skip_nans is needed to protect for traceback NaN Error
            for point_3d in list(pc2.read_points(point_cloud, uvs=points_2d, skip_nans=True)):
                x, y, z = point_3d
                return z

    return None
            

def packageInDistance(point_cloud):
    z = searchForDistanceIn(point_cloud)
    if z is not None:
        rospy.loginfo("Distanze to Object: " + str(z))

        if z < 0.10:
            rospy.loginfo("WARNING: Should not be possible!")
            return False
        elif 0.15 < z < 0.35:
            rospy.loginfo("Package in Range! Start cutting ...")
            return True
        elif z > 0.35:
            rospy.loginfo("No Package in Range")
            return False

    rospy.loginfo("No Distance in PointCloud")
    return False

def callback(msg):  
    global sub_Node
    if packageInDistance(msg):
        # unsubscribe node, messages not needed while cutting
        sub_Node.unregister()
        startCutting()
        sub_Node = rospy.Subscriber("/royale_camera_driver/point_cloud", PointCloud2, callback)



def main():
    global sub_Node

    rospy.init_node('packet_cut', anonymous=True, disable_signals=True)
    sub_Node = rospy.Subscriber("/royale_camera_driver/point_cloud", PointCloud2, callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

