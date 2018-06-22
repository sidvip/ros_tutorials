#!/usr/bin/env python

import rospy
import actionlib
from ros_tutorials.msg import timerAction, timerGoal, timerResult

if __name__ == "__main__":
    rospy.init_node("timer_action_client", anonymous=True)
    client = actionlib.SimpleActionClient('timer', timerAction)
    client.wait_for_server()
    goal = timerGoal()
    goal.time_to_wait = rospy.Duration.from_sec(5.0)
    client.send_goal_and_wait(goal, execute_timeout=rospy.Duration(5))
    print "Time elapsed: %f"%(client.get_result().time_elapsed.to_sec())
