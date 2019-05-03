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
        move = urMove()
        # camera = Camera()
        robot = endeffector()

        # Add a ground to the enviroment
        time.sleep(1)
        move.rviz.addCollisionObjects()
        

        move.group.set_max_velocity_scaling_factor(0.2)
        move.group.set_max_acceleration_scaling_factor(0.5)


        print "--------Go to start Position--------"
        raw_input()
        move.toStartPosition()

        print "------Schneiden------"
        raw_input()
        # move.rviz.add_box("endeffector", position=(-0.4, 0.4, 0.5), box_size=(0.1, 0.1, 0.1), timeout=10)
        # move.rviz.attach_box(timeout=10)
        robot.grab()
        move.toWaypointRelative(posX=0.0, posY=0.50, posZ=0.01, speed=0.02, force=True)

        print "------Nach rechts--------"
        raw_input()
        move.toWaypointRelative(posX=0., posY=-0.01, posZ=0.0, speed=0.05, force=False)
        move.toWaypointRelative(posX=0.4, posY=0.0, posZ=0.0, speed=0.05, force=False)

        
        
        print "-----Paket fallen lassen und Start Position-------"
        raw_input()
        robot.open()
        move.toStartPosition()


        print "------Remove Objects-----"
        move.rviz.removeCollisionObjects()

        print "------Python Skript complete!-----"
        del move

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
  main()