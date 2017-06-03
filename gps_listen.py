#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    gpsdata = data.data.split(",")
    lat,lon,t = gpsdata[0:3]
    hello_str="%f,%f,%f"% (float(lat), float(lon), float(t)) 
    rospy.loginfo(hello_str)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node('gpslistener', anonymous=True)

    rospy.Subscriber("gpschatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
