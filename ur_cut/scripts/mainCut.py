#!/usr/bin/env python

import sys
import copy
import rospy
import urMove
from ur_driver.io_interface import *

def main():
    try:
    
        rospy.init_node('urCut', anonymous=True)
        move = urMove.urMove()

        get_states()
        set_states()

        print "--------Go to start Position--------"
        raw_input()
        move.group.set_max_velocity_scaling_factor(0.05)
        move.toStartPosition()


        print "============ Press `Enter` to execute"
        raw_input()
        set_digital_out(2, True)
        set_digital_out(3, False)
        move.toPoseGoalRelative(0.0, 0.4, 0.0, True)
        raw_input()
        set_digital_out(2, False)
        set_digital_out(3, True)



        print "============ Python Skript complete!"
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
  main()