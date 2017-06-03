from latlongtoutm import *

#Example string
#>$GPGGA,165232.00,5246.90522672,N,00225.75180022,W,5,04,5.7,68.156,M,48.725,M,1.0,0000*66
#nmea="$GPRMC,165232,A,5246.905227,N,00225.751800,W,000.25,71.4,061015,6.4,W,F*19"
#print nmea.split(",")

def read_gps_data(nmea):
	nmea = nmea.split(",")
	#TODO: would be better to use regex instead of split for error handling
	if len(nmea)<8:
		print "error invalid input"
		#if unknown return lat,lon as 0,0 which is a valid cordinate but you will notice the error unless you are in Grewnich
		return 0,0,0
	nmeatype,time,n,lats,hemi,lons,side = nmea[0:7]
        t=float(0)
	#if type is GPRMC calculate lat,lon
	if nmeatype=='$GPRMC':
		t=float(time)
		lat=float(lats)
		latdd=int(lat/100)
		lat=(lat-float(latdd*100))
		lat=lat/60
		lat=lat+float(latdd)

		lon=float(lons)
		londd=int(lon/100)
		lon=(lon-float(londd*100))
		lon=lon/60
		lon=lon+float(londd)
		if side=='w':
			lon=-lon
	else:
		#if not GPRMC ignore
		lat,lon = 0,0
		#TODO use other nmeatypes
	return lat,lon,t

#test function input output
#lat, lon = read_gps_data(nmea)
#print lat, lon
#use zone 23 for UK
#print LLtoUTM(23,lat, lon)
