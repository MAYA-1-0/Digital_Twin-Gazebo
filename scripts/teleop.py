#!/usr/bin/env python3
import math
import rospy
import keyboard
from std_msgs.msg import Float64

rospy.init_node("teleop",anonymous=True)
l_pub=rospy.Publisher("/maya/right_wheel_controller/command",Float64,queue_size=10)
r_pub=rospy.Publisher("/maya/front_wheel_controller/command",Float64,queue_size=10)
b_pub=rospy.Publisher("/maya/left_wheel_controller/command",Float64,queue_size=10)
rate=rospy.Rate(10)


'''print("w -  Forward")
print("d- Left")
print("s-  Stop")
print("a- right")'''

while not rospy.is_shutdown():
	s=str(input())
	if s == "w":
		print("moving forward")
		l_pub.publish(-1)
		r_pub.publish(1)
		b_pub.publish(0)
		rate.sleep()
	elif s == "d":
		print("moving left")
		l_pub.publish(1)
		r_pub.publish(1)
		b_pub.publish(1)
	elif s ==  "s":
		print("stopping")
		l_pub.publish(0)
		r_pub.publish(0)
		b_pub.publish(0)
	elif s == "a":
		print("moving right")
		l_pub.publish(-1)
		r_pub.publish(-1)
		b_pub.publish(-1)
	elif s == "z":
		print("moving backwards")
		l_pub.publish(1)
		r_pub.publish(-1)
		b_pub.publish(0)
	else:
		print("Stopping")
		l_pub.publish(0)
		r_pub.publish(0)
		b_pub.publish(0)
#keyboard.add_hotkey("w",lambda : print("moving forward"))
