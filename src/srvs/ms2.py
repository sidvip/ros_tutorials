#! /usr/bin/env python

import rospy
from termcolor import colored
from ros_tutorials.srv import Add, AddResponse
from operator import add


def add_calculate(request):
    array = request.arrays
    int_array = array.intarray
    float_array = array.floatarray
    print colored(" Service Received ", "cyan", "on_grey", attrs=["bold"])
    print " Request Array received :: {}\n".format(array)
    if len(int_array) == len(float_array):
        added_array = list(map(add, int_array, float_array))
        return AddResponse(added_array)
    else:
        print " Arrays dimensions are mis matched ! :-( "


if __name__ == "__main__":
    rospy.init_node("simple_server1", anonymous=True)
    service = rospy.Service('calculate_addition', Add, add_calculate)
    rospy.spin()