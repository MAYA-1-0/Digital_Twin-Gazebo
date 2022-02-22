# Gazebo Simulation and Control of MAYA
Digital twin is the technical replica of a 3D simulated model in a software and that of a physically built modular prototype.It is a up-to date representation of an actual physical model which replicates every action performed by the 3D simulated model.It is mainly used to evaluate the current position of the robot and receive feedback and predict its future response based on the same. It is basically an actual representation of the robot which is updated by real time data using simulation with respective algorithms,mathematical modelling and PID controls to tune for smooth and optimized performance.

In order to achieve a digital twin of MAYA we have proposed simulink models of the upper body including head and torso designed and built using MATLAB, The base mobile kinematics and motion is simulated in Gazebo . The 3D model is initially designed in Solidworks and further modified as per requirements and exported in MATLAB and Gazebo.Once exported it is tuned with a feedback control loop using PID controls and synchronized accordingly.

Simulation in Gazebo requires a URDF file which is generated from the Design of the robot. Solidworks was used for the design and generating of the URDF file. Gazebo takes into consideration the physics in the underlying object being simulated. In this case a simulation of a three wheeled based Omnidirectional robot is done.
Gazebo provides plugins for differential drive based but as an holonomic wheel base is used, urdf is created using the design from solidworks and cylinders to simulate the function of rollers and rims. And later added the generated urdf parts to it.

-------------------------------------------------------------------------------------------------------------------------------------------

### Usage
1. Clone this repo into "src" of you ROS catkin workspace.
2. Rename the package name to MAYA_BASE (the package was built with this name).
3. cd to workspace and run catkin_make


Once the workspace is ready,
1. Open a terminal (alternatively press Ctrl+Alt+T) and type
```
roslaunch MAYA_BASE gazebo.launch
```



-------------------------------------------------------------------------------------------------------------------------------------------

######              Imported URDF Model in Gazebo
![Imported URDF Model in Gazebo](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-17%2020-27-57.png)
![Imported URDF Model in Gazebo](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-17%2020-28-05.png)


For Simulating in real time, subscribe to Topic base/goal from the navigation stack and same is published to respective 3 wheel topics /maya/wheel_controller/command in gazebo

![Rqt Graph representing URDF Joints](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-22%2021-54-35.png)

![Controller Nodes for Simulation]()
![Gazeo world Model]()









