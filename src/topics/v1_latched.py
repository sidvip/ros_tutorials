#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
    rospy.init_node("publisher_node_v1", anonymous=True)
    pub = rospy.Publisher('tick_tock', Bool, queue_size=5, latch=True)
    rate = rospy.Rate(2)
    init_bool = True
    pub.publish(init_bool)
    init_bool = False
    pub.publish(init_bool)
    rate.sleep()
    rospy.spin()