#!/usr/bin/env python3
import math

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


move_robot = Twist()
move_robot.linear.x = 0.5 # Move forward at 0.2 m/s
move_robot.angular.z = 0.0 # No rotation
def callback(msg):
    pu.publish(move_robot)
    # center_index = len(msg.ranges) // 2
    # center_distance = msg.ranges[center_index]
    # if math.isinf(center_distance) or math.isnan(center_distance):
    #     center_distance = 5.0
    valid = [r for r in msg.ranges if not math.isinf(r) and not math.isnan(r)]
    center_distance = min(valid)
    if (center_distance < 0.3):
        move_robot.linear.x = 0.0# Stop moving forward
        move_robot.angular.z = 0.5 # Rotate at 0.5 rad/s
    elif (center_distance > 4):
        move_robot.linear.x = 0.2 # Move forward at 0.2 m/s
        move_robot.angular.z = 0.0 # No rotation

    print("Distance to obstacle: {:.2f} m".format(center_distance))
rospy.init_node('lidar_motion')
pu= rospy.Publisher('/cmd_vel', Twist, queue_size=1)
su = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()