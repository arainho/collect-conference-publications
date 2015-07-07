__author__ = 'raimaz'

from bs4 import BeautifulSoup
import urllib2
import wget

#my_url= input("Enter a website to extract publications from")
my_url="http://alcatel-lucent.cvent.com/Surveys/Questions/SurveyMain.aspx?r=8a6cedab-dbe0-442d-a76f-c4ef13035c14&ma=1"
my_content = urllib2.urlopen(my_url).read()

my_soup = BeautifulSoup(my_content, "lxml")
#print my_soup.prettify()

for my_item in my_soup:
    tags = my_soup.findAll('a')
    tags_content= my_soup.a
    file_name = tags_content.contents[0]+".pdf"
    my_links = tags["href"]
    print(my_links, file_name)
    #wget.download(my_links, file_name)
pass

