import json
import urllib2
import os

radarurl = "http://metservice.com/publicData/rainRadarAuckland_2h_7min_300K"

data = json.load(urllib2.urlopen(radarurl))

for item in data:
		validFromRaw = item['validFromRaw']
                validFromRaw = str(validFromRaw)
                print validFromRaw
                shortDateTime = item['shortDateTime']
		jpg = "/var/www/house/dashboard/publicData/" + validFromRaw + '.jpg'
                print jpg

		fullurl = "http://www.metservice.com" + item['url']
		
		response = urllib2.urlopen(fullurl)

		#open the file for writing
		fh = open(jpg, "wb")

		# read from request while writing to file
		fh.write(response.read())
		fh.close()

                convertjpg = "convert -gravity Center " + jpg + " -crop 70%x+0+0 " + jpg

		os.system(convertjpg)

                labeljpg = "convert -pointsize 20 -fill yellow -draw 'text 20,400 \"" + shortDateTime +  "\"' " + jpg + " " + jpg
                print labeljpg

		os.system(labeljpg)

os.system("convert -delay 50 /var/www/house/dashboard/publicData/* /var/www/house/dashboard/radar.gif")
os.system("rm /var/www/house/dashboard/publicData/*")


isobars = "http://metservice.com/publicData/tasmanSeaCombinedCharts"

isodata = json.load(urllib2.urlopen(isobars))

w = isodata['imageData']

isobarimage = w[3]['url'] 

fullisourl = "http://www.metservice.com" + isobarimage

isojpg = "/var/www/house/dashboard" + isobarimage

isoresponse = urllib2.urlopen(fullisourl)

fh = open('/var/www/house/dashboard/isobars.jpeg', "wb")

# read from request while writing to file
fh.write(isoresponse.read())
fh.close()

convertjpg = "convert -gravity Center /var/www/house/dashboard/isobars.jpeg -crop 80%x+0+0 /var/www/house/dashboard/isobars.jpeg"
os.system(convertjpg)
