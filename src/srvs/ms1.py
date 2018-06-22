#! /usr/bin/env python

import rospy
from ros_tutorials.srv import Square, SquareResponse


def square_calculate(request):
    array = request.num
    print " Request Array received :: {}".format(array)
    sq_list = []
    for i in array:
        sq_list.append(i**2)
    return SquareResponse(sq_list)


if __name__ == "__main__":
    rospy.init_node("simple_server1", anonymous=True)
    service = rospy.Service('calculate_square', Square, square_calculate)
    rospy.spin()
