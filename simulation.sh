#!/bin/bash
xterm -e "roslaunch ur_gazebo ur10.launch" &
sleep 10s
xterm -e "roslaunch ur10_moveit_config ur10_moveit_planning_execution.launch sim:=true" &
sleep 5s
xterm -e "roslaunch ur10_moveit_config moveit_rviz.launch config:=true" &
