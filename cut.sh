#!/bin/bash
xterm -e "roslaunch ur_bringup ur10_bringup.launch robot_ip:=192.168.3.2" &
sleep 5s
xterm -e "roslaunch ur10_moveit_config ur10_moveit_planning_execution.launch" &
sleep 3s
xterm -e "roslaunch ur10_moveit_config moveit_rviz.launch config:=true" &
sleep 5s
xterm -e "roslaunch ur_cut pico_flexx_driver.launch" &
sleep 1s
xterm -e "rosrun ur_cut mainCut.py" &
