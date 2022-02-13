import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

lin=0
ang=0

def curr_cb(msg1):
	global lin,ang
	curr_lin=msg1.linear.x
	curr_ang=msg1.angular.z
	while not ang-curr_ang<=0.03:
		if ang<0: #left turn
			l_pub.publish(1)
	                r_pub.publish(1)
        	        b_pub.publish(1)
		elif ang>0: #turn right
			l_pub.publish(-1)
	                r_pub.publish(-1)
        	        b_pub.publish(-1)
		else:
			l_pub.publish(0)
	                r_pub.publish(0)
        	        b_pub.publish(0)

	while not lin-curr_lin <= 0.03:
		l_pub.publish(-1)
		r_pub.publish(1)
		b_pub.publish(0)
	l_pub.publish(0)
        r_pub.publish(0)
        b_pub.publish(0)


def mv_cb(msg):
	global lin,ang
	lin=msg.lin.x
	ang=msg.angular.z

rospy.init_node("gazebo_maya_twin",anonymous=True)
l_pub=rospy.Publisher("/maya/right_wheel_controller/command",Float64,queue_size=10)
r_pub=rospy.Publisher("/maya/front_wheel_controller/command",Float64,queue_size=10)
b_pub=rospy.Publisher("/maya/left_wheel_controller/command",Float64,queue_size=10)
rate=rospy.Rate(10)
rospy.Subscriber("/base/goal",Twist,mv_cb)
rospy.Subscriber("/base/current_pose",Twist,curr_cb)
