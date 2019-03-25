#!/usr/bin/env python

###########################################################
#   Import
###########################################################
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



###########################################################
#   Variables and Objects
###########################################################
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('schneiden1',anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)
global scale
scale = 1
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

###########################################################
#   Functions
###########################################################

def initPosition():
    waypoints=[]
    wpose = copy.deepcopy(group.get_current_pose().pose)
    
    # Ausgangsposition einnehmen: 
    wpose.position.x = 0.0
    wpose.position.y = 0.3
    wpose.position.z = 0.5
    
    # Greifer 90 grad um die y-achse und 30 grad um die x-achse drehen:

    # Orientierung mit berechnung
    # q8a = Quaternion(w=0.707, x=0, y=0.707, z=0)
    # q8b = Quaternion(w=0,x=-0,y=0,z=0)
    # quaternion = Quaternion.multiply(q8a,q8b)
    # wpose.orientation.x =quaternion[1]  #richtige position
    # wpose.orientation.y =quaternion[2]
    # wpose.orientation.z =quaternion[3]
    # wpose.orientation.w =quaternion[0]

    # Orientierung manuell gesetzt
    wpose.orientation.x = 0.0
    wpose.orientation.y = 0.0
    wpose.orientation.z = 0.707
    wpose.orientation.w = 0.707

    
    waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
    (plan, fraction) = group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold

    executePath(plan)

def relativePosition(posX = None, posY = None, posZ = None):
    waypoints=[]
    wpose = copy.deepcopy(group.get_current_pose().pose)
    
    wpose.position.x += posX
    wpose.position.y += posY
    wpose.position.z += posZ
    
    waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
    (plan, fraction) = group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold

    executePath(plan)  


######################
#   Weg planen und ausfuehren
######################

def executePath(plan):
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    # Publish
    display_trajectory_publisher.publish(display_trajectory)

    #print "Press ENTER to execute the next Path-Waypoint"
    #raw_input()
    time.sleep(5)
    group.execute(plan, wait=True)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    group.clear_pose_targets()

def grap(var):
    set_digital_out(2, var)
    set_digital_out(3, not var)


def main():
    try:
        # We can get a list of all the groups in the robot:
        group_names = robot.get_group_names()
        print "============ Robot Groups:", robot.get_group_names()
        print "testing io-interface"
        get_states()
        print "listener has been activated"
        set_states()
        print "service-server has been started"
        

        ######################
        # Init of Start Position
        #####################
        initPosition()
        #####################

        #####################
        # Roboter ablauf
        #####################
        # for x in range(0,1):
        #     grap(True)
        #     relativePosition(0.0, 0.4, 0.0)
        #     relativePosition(0.4, 0.0, 0.0)
        #     grap(False)
        #     initPosition()




        print "Neue Position"
        print copy.deepcopy(group.get_current_pose().pose)

    except rospy.ROSInterruptException:
        return

if __name__ == '__main__':
    main()