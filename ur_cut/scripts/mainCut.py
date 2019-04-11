#!/usr/bin/env python

import sys
import copy
import rospy
from urMove import urMove
from endeffector import endeffector

def main():
    try:

        move = urMove()

        move.rviz.addGround()


        print "--------Go to start Position--------"
        raw_input()
        move.toStartPosition()



       

        print "------Press `Enter` to execute------"
        raw_input()
        endeffector.grab()
        move.group.set_max_velocity_scaling_factor(0.1)
        move.toPoseGoalRelative(0.0, 0.4, 0.0, force=False)
        
        print "-----Paket fallen lassen-------"
        raw_input()
        endeffector.open()


        print "------Python Skript complete!-----"
        
        move.rviz.removeGround()
        del move

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
  main()