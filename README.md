# PacketCutStudien

This repository contains a ROS Catkin package for opening packets with an UR10. 

## Getting Started

Following these steps will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Setting up your environment by installing ROS with a Catkin workspace on Ubuntu 16.04. For further information see [http://wiki.ros.org/kinetic/Installation/Ubuntu](http://wiki.ros.org/kinetic/Installation/Ubuntu).
 
This project uses several other ROS packages. Clone them into your workspace with:

```
cd ~/catkin_ws/src
git clone https://github.com/MobMonRob/pd_ur10.git
git clone https://github.com/MobMonRob/pd_edgedetection.git
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

The packet cut can be started by launching the launchfile:

```
roslaunch ur_cut cut.launch
```

## License

This project is licensed under the BSD License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This project uses code from ROS tutorial und MeveIt
