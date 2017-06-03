#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import String
prevlat=0
prevlon=0
prevti=0
vel=0.0
dataready=0
def callback(data):
    global prevlat
    try:
        prevlat
    except NameError:
        prevlat = 0
    global prevlon
    try:
        prevlon
    except NameError:
        prevlon = 0
    global prevti
    try:
        prevti
    except NameError:
        prevti = 0

    global vel
    global dataready
    gpsdata = data.data.split(",")
    lat,lon,t = gpsdata[0:3]
    lt=float(lat)
    ln=float(lon)
    ti=float(t)
    dist=math.sqrt((lt-prevlat)*(lt-prevlat)+(ln-prevlon)*(ln-prevlon));
    diffti=ti-prevti
    vel=dist/diffti
    hello_str="Vel= %f,%f"% (vel,diffti) 
    #rospy.loginfo(hello_str)
    prevlat=lt
    prevlon=ln
    prevti=ti
    dataready=1
  
def listener():
    global dataready
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node('gpsvel', anonymous=True)

    rospy.Subscriber("gpschatter", String, callback)
    pub = rospy.Publisher('velchatter', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    dataready=0
    # spin() simply keeps python from exiting until this node is stopped
    while not rospy.is_shutdown():
        if dataready==1:
            hello_str = "%f" % vel
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            dataready=0
        rate.sleep()

if __name__ == '__main__':
    listener()

