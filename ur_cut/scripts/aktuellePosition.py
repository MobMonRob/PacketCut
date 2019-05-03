#!/usr/bin/env python
import sys
import time
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('schneiden1',anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)
scale = 1

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)

# We can get the name of the reference frame for this robot:
planning_frame = group.get_planning_frame()
print "============ Reference frame: %s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = group.get_end_effector_link()
print "============ End effector: %s" % eef_link

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "============ Robot Groups:", robot.get_group_names()

print(group.get_goal_tolerance())

# Sometimes for debugging it is useful to print the entire state of the
# robot:
#print "============ Printing robot state"
#print robot.get_current_state()
#print ""

####################
#Einstellen der Gelenkwinkel
####################

# We can get the joint values from the group and adjust some of the values:
# joint_goal = group.get_current_joint_values()
# joint_goal[0] = 0
# joint_goal[1] = -pi/4
# joint_goal[2] = 0
# joint_goal[3] = -pi/2
# joint_goal[4] = 0
# joint_goal[5] = pi/3
# joint_goal[6] = 0

####################
#Einstellen der Koordinaten
####################

# pose_goal = geometry_msgs.msg.Pose()

# print geometry_msgs.msg.Pose()

# pose_goal.orientation.w = 0.0
# pose_goal.position.x = -0.2
# pose_goal.position.y = 0.0
# pose_goal.position.z = 0.0
# group.set_pose_target(pose_goal)


######################
# Carthesian Path
######################



wpose = group.get_current_pose().pose
print wpose
