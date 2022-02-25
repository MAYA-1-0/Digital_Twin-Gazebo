# Gazebo Simulation and Control of MAYA
Digital twin is the technical replica of a 3D simulated model in a software and that of a physically built modular prototype.It is a up-to date representation of an actual physical model which replicates every action performed by the 3D simulated model.It is mainly used to evaluate the current position of the robot and receive feedback and predict its future response based on the same. It is basically an actual representation of the robot which is updated by real time data using simulation with respective algorithms,mathematical modelling and PID controls to tune for smooth and optimized performance.

In order to achieve a digital twin of MAYA we have proposed simulink models of the upper body including head and torso designed and built using MATLAB, The base mobile kinematics and motion is simulated in Gazebo . The 3D model is initially designed in Solidworks and further modified as per requirements and exported in MATLAB and Gazebo.Once exported it is tuned with a feedback control loop using PID controls and synchronized accordingly.

Simulation in Gazebo requires a URDF file which is generated from the Design of the robot. Solidworks was used for the design and generating of the URDF file. Gazebo takes into consideration the physics in the underlying object being simulated. In this case a simulation of a three wheeled based Omnidirectional robot is done.
Gazebo provides plugins for differential drive based but as an holonomic wheel base is used, urdf is created using the design from solidworks and cylinders to simulate the function of rollers and rims. And later added the generated urdf parts to it.

-------------------------------------------------------------------------------------------------------------------------------------------

### Usage and System Requirements
Requires ROS Melodic (Along with Gazebo and other necessary tools) , Python2 installed in Ubuntu(18.04) System 
1. Clone this repo into "src" of you ROS catkin workspace.
2. Rename the package name to MAYA_BASE (the package was built with this name).
3. cd to workspace and run catkin_make


Once the workspace is ready,
1. Open a terminal (alternatively press Ctrl+Alt+T) and type
```
roslaunch MAYA_BASE gazebo.launch
```

2. Below will list all the controller topics running
```
rostopic list
```
![img](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-25%2018-38-14.png)


3. To move the Robot, command velocities can be published to topics directly
```
rostopic pub maya/<controller_name_here>/command std_msgs/Float64 "data: 0.0"
```

4. teleop.py scripts can also be used to control the robot from keyboard.
```
rosrun MAYA_BASE teleop.py
```

5. For running the digital Twin run the below script after getting [kinematics](https://github.com/MAYA-1-0/KInematics_And_Odometry) started.
```
rosrun MAYA_BASE digital_twin.py 
```


-------------------------------------------------------------------------------------------------------------------------------------------

######              Imported URDF Model in Gazebo
![Imported URDF Model in Gazebo](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-17%2020-27-57.png)
![Imported URDF Model in Gazebo](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-17%2020-28-05.png)


For Simulating in real time, subscribe to Topic base/goal from the navigation stack and same is published to respective 3 wheel topics /maya/wheel_controller/command in gazebo

######   Rqt Graph representing URDF Joints
![Rqt Graph representing URDF Joints](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-22%2021-54-35.png)


######  Controller Nodes for Simulation
![Controller Nodes for Simulation](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-22%2021-54-55.png)


######  Gazeo world Model
![Gazeo world Model](https://github.com/MAYA-1-0/Digital_Twin-Gazebo/blob/main/images/Screenshot%20from%202022-02-22%2021-56-38.png)









