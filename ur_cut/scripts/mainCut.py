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
        

        move.group.set_max_velocity_scaling_factor(0.05)
        move.group.set_max_acceleration_scaling_factor(1)


        print "--------Go to start Position--------"
        raw_input()
        move.toStartPosition()

        print "------Schneiden------"
        raw_input()
        # move.rviz.add_box("endeffector", position=(-0.4, 0.4, 0.5), box_size=(0.1, 0.1, 0.1), timeout=10)
        # move.rviz.attach_box(timeout=10)
        robot.grab()

        # move.toPoseGoalRelative(0.0, 0.44, 0.0, force=False)
        move.toWaypointRelative(0.0, 0.44, 0.01)

        # move.toPoseGoalRelative(0.0, 0.1, 0.0, force=False)
        # move.toPoseGoalRelative(0.0, 0.1, 0.0, force=False)
        # move.toPoseGoalRelative(0.0, 0.1, 0.0, force=False)
        # move.toPoseGoalRelative(0.0, 0.1, 0.0, force=False)
        # move.toPoseGoalRelative(0.0, 0.04, 0.0, force=False)

        # print "------Nach rechts--------"
        # raw_input()
        # move.toPoseGoalRelative(0.1, 0.0, 0.0, force=False)
        # move.toPoseGoalRelative(0.1, 0.0, 0.0, force=False)
        # move.toPoseGoalRelative(0.1, 0.0, 0.0, force=False)
        # move.toPoseGoalRelative(0.1, 0.0, 0.0, force=False)

        # move.toWaypointRelative(0.4, 0.0, 0.0)
        
        
        print "-----Paket fallen lassen und Start Position-------"
        raw_input()
        robot.open()
        move.toStartPosition()


        print "------Python Skript complete!-----"
        
        move.rviz.removeCollisionObjects()
        del move

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
  main()