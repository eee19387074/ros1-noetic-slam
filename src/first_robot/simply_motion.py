#!/usr/bin/env python3
from geometry_msgs import msg
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node('motion')
rate = rospy.Rate(5) # 10 Hz
move_cmd= Twist()
move_cmd.linear.x = 0.2 # Move forward at 0.5 m/s
# su = rospy.Subscriber('/scan', LaserScan,callback)
pu = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
Forward = True

while not rospy.is_shutdown():
    if Forward:
        move_cmd.linear.x = 0.2 # Move forward at 0.5 m/s
    else:
        move_cmd.linear.x = -0.2 # Move backward at 0.5 m/s 
    pu.publish(move_cmd)
    # forward = not forward # Toggle direction
    rate.sleep()