#!/usr/bin/env python

###########################################################
#   Import
###########################################################
import sys
import copy
import rospy
from urMove import urMove
from endeffector import endeffector
from camera import Camera
import time

###########################################################
#   Main - Function
###########################################################
def main():
    try:
        ###################################
        # Initialization
        ###################################
        move = urMove()
        # camera = Camera()
        robot = endeffector()

        # Add a ground to the enviroment
        time.sleep(1)
        move.rviz.addCollisionObjects()
        
        # Set velocity and acceleration 
        move.group.set_max_velocity_scaling_factor(0.2)
        move.group.set_max_acceleration_scaling_factor(1)


        # while True:
        #     print camera.getDistance()
        #     pass
        

        ####################################
        # Main Cut 
        ####################################
        print "--------Go to start Position--------"
        raw_input()
        move.toInitPosition()

        print "--------Schneiden-------------------"
        raw_input()
        robot.grab()
        move.toWaypointRelative(posX=0.0, posY=0.30, posZ=0.0, speed=0.02, force=False)
        move.toWaypointRelative(posX=0.0, posY=0.05, posZ=0.0, speed=0.02, force=True)

        print "--------Nach rechts-----------------"
        raw_input()
        move.toWaypointRelative(posX=0.0, posY=-0.01, posZ=0.0, speed=0.02, force=False)
        move.toWaypointRelative(posX=0.4, posY=0.0, posZ=0.0, speed=0.02, force=False)

        print "--------Paket fallen lassen---------"
        raw_input()
        robot.open()
        move.toStartPosition()


        print "--------Remove Objects--------------"
        move.rviz.removeCollisionObjects()

        print "--------Python Skript complete!-----"
        del move

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
  main()