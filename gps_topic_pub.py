#!/usr/bin/env python


import rospy
import serial
from std_msgs.msg import String
from nmea_split import *
from latlongtoutm import *
import time

def gps_srv():
    s = serial.Serial()
    s.port = "/dev/ttyACM0" #for arduino /dev/ttyACM0
    s.baudrate = 4800
    pub = rospy.Publisher('gpschatter', String, queue_size=10)
    rospy.init_node('gpspub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	    s.open()
	    while True:
	    	nmea=s.readline()
		lat, lon,t = read_gps_data(nmea)
		if lat<>0 and lon<>0:
			break
	    s.close()
	    
	    print "Read serial"
	    c,lt,ln = LLtoUTM(23,lat, lon)
	    hello_str = "%f,%f,%s" % (lt, ln, rospy.get_time() ) 
	    rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
	    
if __name__ == '__main__':
    try:
        gps_srv()
    except rospy.ROSInterruptException:
        pass

