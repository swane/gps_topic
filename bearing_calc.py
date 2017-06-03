#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from math import pi, sin, cos, tan, sqrt, atan2

fE=0
fN=0

global last_fN
last_fN=5848133.0
global last_fE
last_fE=463524.0



def callback(data):
    global fE
    global fN
    gpsdata = data.data.split(",")
    lat,lon,t = gpsdata[0:3]
  #  hello_str="%f,%f,%f"% (float(lat), float(lon), float(t)) 
    fE=float(lat)
    fN=float(lon)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    
    
    rospy.init_node('bearing_calc',anonymous=False)

    rospy.Subscriber("gpschatter", String, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

def dist_bearing(StN,StE,EnN,EnE):
	dist=sqrt(((EnN-StN)*(EnN-StN))+((EnE-StE)*(EnE-StE)))
	bearing=atan2((EnE-StE),(EnN-StN))
	bearing=bearing*57.29578
	if bearing<0:
		bearing=360+bearing
	return (dist, bearing)

def bearing_calc():
	global last_fN
	global last_fE
	global fN
	global fE
	#Read the GPS location from the subscription
	dist, bearing=dist_bearing(last_fN,last_fE,fN,fE)
	print "Hello, I'm at: %f, %f" % (fE, fN)
	
	if dist>10:
		print "Dist>10 so: dist=%f, bearing=%f" % (dist, bearing)
		last_fN=fN
		last_fE=fE
	rospy.sleep(1)

if __name__ == '__main__':
	listener()
	while True:
		bearing_calc()




