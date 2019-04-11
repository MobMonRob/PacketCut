#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from ur_driver.io_interface import *
import numpy as numpy
import time
from pyquaternion import *
from geometry_msgs.msg import Vector3


class endeffector(object):
    def __init__(self):
        super(endeffector, self).__init__()

        get_states()
        set_states()
        self.grab(False)


    def __del__(self):

    def grab(self):
        set_digital_out(2, True)
        set_digital_out(3, False)

    def open(self):
        set_digital_out(2, False)
        set_digital_out(3, True)

     

    pass