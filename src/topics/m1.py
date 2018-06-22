#! /usr/bin/env python

import rospy
from std_msgs.msg import Bool

count = 0


def callback(msg):
    global count
    if msg.data == True:
       count +=1
       print " Number :: {}".format(count)
    else:
        print "Don't send me False messages"


if __name__ =="__main__":
    rospy.init_node("m1_subscriber_m1", anonymous=True)
    sub = rospy.Subscriber("/tick_tock", Bool, callback)
    rospy.spin()
