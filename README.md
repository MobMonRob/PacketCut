# PacketCutStudien

This repository contains a ROS Catkin package for opening packets with an UR10. 

## Getting Started

Following these steps will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Setting up your environment by installing ROS with a Catkin workspace on Ubuntu 16.04. For further information see [http://wiki.ros.org/kinetic/Installation/Ubuntu](ROS kinetic Ubuntu Installation).
Afterwards install MoveIt!: [https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html](MoveIt Getting Started)
 
This project uses the pd_ur10 project from MobMonRob. Clone it into your workspace with:

```
cd ~/catkin_ws/src
git clone https://github.com/MobMonRob/pd_ur10.git
```

A pico flexx ToF camera is used to detect the packages. For usage of the camera the royale SDK is needed. See [https://github.com/MobMonRob/pd_edgedetection](https://github.com/MobMonRob/pd_edgedetection) for more information.

### Installing

To install the package simply clone this project into your Catkin workspace and build it:

```
cd ~/catkin_ws/src
git clone https://github.com/MobMonRob/PacketCutStudien.git
catkin build
```

## Usage

Simply start the project by executing the cut.sh script. It will launch all needed files in seperate xTerm windows. You might have to adjust the IP-Adress from the Robot within the file.

```
cd ~/catkin_ws/src/PacketCutStudien
./cut.sh
```

Or launch all files manually. 
First for controlling the Robot launch the files from [https://github.com/MobMonRob/pd_ur10.git](pd_ur10)
Then start the Pico Flexx drivers:

```
roslaunch ur_cut pico_flexx_driver.launch
```

And start the cutting with:

```
rosrun ur_cut mainCut.py
```

## Acknowledgments

* This project uses code from ROS tutorial und MoveIt
* It is also build on the previously mentioned pd_ur10 repository
