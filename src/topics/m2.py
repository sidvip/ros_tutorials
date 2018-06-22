#! /usr/bin/env python

import rospy
from ros_tutorials.msg import new_msg


def callback(msg):
    print " Integer array received :: {}".format(msg.intarray)
    print "Float array received :: {}".format(msg.floatarray)


if __name__ =="__main__":
    rospy.init_node("m1_subscriber_m2", anonymous=True)
    sub = rospy.Subscriber("/tick_tock", new_msg, callback)
    rospy.spin()