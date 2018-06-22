#!/usr/bin/env python
import rospy
from random import *
from ros_tutorials.msg import new_msg

if __name__ == "__main__":
    rospy.init_node("publisher_node_v2", anonymous=True)
    pub = rospy.Publisher('tick_tock', new_msg, queue_size=5)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = new_msg()
        msg.intarray = [int(random()*20), int(random()*30), int(random()*40)]
        msg.floatarray = [random(), random(), random()]
        pub.publish(msg)
        rate.sleep()