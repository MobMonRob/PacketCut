#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import roslib; roslib.load_manifest('ur_driver')
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *
from ur_driver.io_interface import *
import numpy as numpy
import time
import edge_detection_pmd.msg
from pyquaternion import *
from geometry_msgs.msg import Vector3
import socket
import threading