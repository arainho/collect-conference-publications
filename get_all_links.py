__author__ = 'raimaz'

import urllib2
import re

url="http://alcatel-lucent.cvent.com/Surveys/Questions/SurveyMain.aspx?r=8a6cedab-dbe0-442d-a76f-c4ef13035c14&ma=1"

#connect to a URL
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print links
