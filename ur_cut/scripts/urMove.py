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
from pyquaternion import *
from geometry_msgs.msg import Vector3
from forceTorque import forceTorque
import threading
from rviz import rvizCollision



class urMove(object):
    def __init__(self):
        super(urMove, self).__init__()

        ## First initialize `moveit_commander`_ and a `rospy`_ node:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('urMove', anonymous=True)

        ## Instantiate a `RobotCommander`_ object. This object is the outer-level interface to
        ## the robot:
        robot = moveit_commander.RobotCommander()
        
        ## Instantiate a `PlanningSceneInterface`_ object.  This object is an interface
        ## to the world surrounding the robot:
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
        ## to one group of joints.  In this case the group is the joints in the UR10
        ## arm so we set ``group_name = manipulator``. If you are using a different robot,
        ## you should change this value to the name of your robot arm planning group.
        ## This interface can be used to plan and execute motions on the UR10:
        group_name = "manipulator"
        group = moveit_commander.MoveGroupCommander(group_name)
        
    
        ## We create a `DisplayTrajectory`_ publisher which is used later to publish
        ## trajectories for RViz to visualize:
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                    moveit_msgs.msg.DisplayTrajectory,
                                                    queue_size=20)

        
        # We can get the name of the reference frame for this robot:
        planning_frame = group.get_planning_frame()

        # We can also print the name of the end-effector link for this group:
        eef_link = group.get_end_effector_link()

        # We can get a list of all the groups in the robot:
        group_names = robot.get_group_names()

        # Start the ForceTorque Sensor 
        forceSensor = forceTorque()

        # Start the CollisionObjects in RVIZ
        rviz = rvizCollision(robot, scene, group)
        
        
        # Misc variables
        self.robot = robot
        self.scene = scene
        self.group = group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names
        self.forceSensor = forceSensor
        self.rviz = rviz


    # Deconstructor for the urMove - Class 
    def __del__(self):
        return
        

    # Start position for the robot
    def toStartPosition(self):

        pose_goal = geometry_msgs.msg.Pose()
        pose_goal = self.group.get_current_pose().pose

        #self.group.
        pose_goal.position.x = -0.4
        pose_goal.position.y = 0.4
        pose_goal.position.z = 0.48

        pose_goal.orientation.x = 0.0
        pose_goal.orientation.y = 0.0
        pose_goal.orientation.z = 0.707
        pose_goal.orientation.w = 0.707

        self.group.set_pose_target(pose_goal)

        # Go to new position
        self.group.go(wait=True)
        # After Mmving you have to stop the Robot
        self.group.stop()
        # It is always good to clear your targets after planning with poses.
        self.group.clear_pose_targets()

        return

    # Function for getting information about the ForceTorque Sensor 
    # and stop the Robot after fz is over 4N 
    def stopPoseGoalByForce(self):
        refX, refY, refZ = 0, 0, 0
        for i in range(10):
            refXTemp, refYTemp, refZTemp = self.forceSensor.getForce()
            refZ += refZTemp
            time.sleep(0.2)
            pass
        
        refZ = (refZ/10)+2
        print "Schwellwert: "
        print(refZ)
        refState = self.group.get_current_pose().pose
        refState = round(refState.position.x, 5) + round(refState.position.y, 5) + round(refState.position.z, 5)
        time.sleep(1)
        while True:
            fx,fy,fz = self.forceSensor.getForce()
            print (fz)
            #TODO Value from Config-File
            if fz <= (refZ - 8):
                print ("Barriere erkannt")
                print "Schwellwert: "
                print(refZ)
                self.group.stop()
                break
            newState = self.group.get_current_pose().pose
            newState = round(newState.position.x, 5) + round(newState.position.y, 5) + round(newState.position.z, 5)
            print newState
            # if (refState == newState):
            #     return -1
            # else:
            #     refState = newState
            #     pass
            pass

    # Function to move the Robot in a relative position
    def toPoseGoalRelative(self, posX = None, posY = None, posZ = None, force = False):

        ## Planning to a Pose Goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        ## We can plan a motion for this group to a desired pose for the
        ## end-effector:
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal = self.group.get_current_pose().pose
        
        # setting the new position
        pose_goal.position.x += posX
        pose_goal.position.y += posY
        pose_goal.position.z += posZ
        self.group.set_pose_target(pose_goal)

        #TODO Test auf threading und Execution
        self.group.go(wait=not force)

        # If you will use the force sensor to stop the robot,
        # the thread will start to get information of the sensor
        if force == True:
            if self.stopPoseGoalByForce() == -1:
                print "Zu weit gefahren kein widerstand"
                pass
            pass
   
    # Function to move the Robot in an absolute position
    def toPoseGoalAbsolute(self, posX = None, posY = None, posZ = None, force = False):

        ## Planning to a Pose Goal
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        ## We can plan a motion for this group to a desired pose for the
        ## end-effector:
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal = self.group.get_current_pose().pose
        
        # setting the new position
        pose_goal.position.x = posX
        pose_goal.position.y = posY
        pose_goal.position.z = posZ
        self.group.set_pose_target(pose_goal)

        #TODO Test auf threading und Execution
        self.group.go(wait=not force)

        # If you will use the force sensor to stop the robot,
        # the thread will start to get information of the sensor
        if force == True:
            if self.stopPoseGoalByForce() == -1:
                print "Zu weit gefahren kein widerstand"
                pass
            pass

    def toWaypointRelative(self, posX = None, posY = None, posZ = None, speed = 1.0, force = False):


        waypoints=[]
        wpose = copy.deepcopy(self.group.get_current_pose().pose)
        
        wpose.position.x += posX
        wpose.position.y += posY
        wpose.position.z += posZ
        
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
        (plan, fraction) = self.group.compute_cartesian_path(
                                        waypoints,   # waypoints to follow
                                        0.01,        # eef_step
                                        0.0)         # jump_threshold


        self.display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        self.display_trajectory.trajectory_start = self.robot.get_current_state()
        self.display_trajectory.trajectory.append(plan)
        
	    # Publish
        self.display_trajectory_publisher.publish(self.display_trajectory)

        newPlan = self.group.retime_trajectory(self.robot.get_current_state(), plan, speed)

        self.group.execute(newPlan, wait=not force)
        
        if force == True:
            if self.stopPoseGoalByForce() == -1:
                print "Zu weit gefahren kein widerstand"
                pass
            pass


    pass
