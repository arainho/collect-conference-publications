__author__ = 'raimaz'

from bs4 import BeautifulSoup
import urllib2
import wget

#my_url= input("Enter a website to extract publications from")
my_url="http://alcatel-lucent.cvent.com/Surveys/Questions/SurveyMain.aspx?r=8a6cedab-dbe0-442d-a76f-c4ef13035c14&ma=1"
my_website = urllib2.urlopen(my_url)
my_html = my_website.read()

my_soup = BeautifulSoup(my_html, "lxml")

print(my_soup)

