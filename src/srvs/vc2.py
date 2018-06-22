#! /usr/bin/env python

import rospy
from ros_tutorials.srv import Add
from ros_tutorials.msg import *
from random import *

if __name__ == "__main__":
    rospy.init_node("simple_client2", anonymous=True)
    rospy.wait_for_service('calculate_addition')
    data = new_msg()
    data.intarray = [randint(5,11), randint(11,20), randint(25,35)]
    data.floatarray = [random()*10+1, random()*30+20, random()*20+10 ]
    word_counter = rospy.ServiceProxy('calculate_addition', Add)
    added_array = word_counter(arrays=data)
    print " Addition of array elements :: {}\n".format(added_array.addedarray)

