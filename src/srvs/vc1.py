#! /usr/bin/env python

import rospy
from ros_tutorials.srv import Square
from random import *

if __name__ == "__main__":
    rospy.init_node("simple_client1", anonymous=True)
    rospy.wait_for_service('calculate_square')
    while not rospy.is_shutdown():
        request_array = []
        for i in range(randint(0, 6)):
            request_array.append(randint(0, 11))
        word_counter = rospy.ServiceProxy('calculate_square', Square)
        square_array = word_counter(num=request_array)
        print " Square of array elements :: {}".format(square_array.square)

