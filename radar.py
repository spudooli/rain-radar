import json
import urllib2
import os

radarurl = "http://metservice.com/publicData/rainRadarAuckland_2h_7min_300K"

data = json.load(urllib2.urlopen(radarurl))

for item in data:
		
		jpg = "/var/www/house/dashboard" + item['url']

		fullurl = "http://www.metservice.com" + item['url']
		
		response = urllib2.urlopen(fullurl)

		#open the file for writing
		fh = open(jpg, "wb")

		# read from request while writing to file
		fh.write(response.read())
		fh.close()

		convertjpg = "convert -gravity Center " + jpg + " -crop 70%x+0+0 " + jpg
		os.system(convertjpg)

os.system("convert -delay 100 /www/data/house/dashboard/IcePics/ob/*.jpeg /www/data/house/dashboard/IcePics/ob/radar.gif")
os.system("rm /www/data/house/dashboard/IcePics/ob/*.jpeg")

