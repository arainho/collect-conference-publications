#encoding=utf-8
__author__ = 'Andre Rainho '
__email__ = 'arainho.it@gmail.com'

from bs4 import BeautifulSoup
import urllib2
import wget

my_url = raw_input("Enter a website to extract pdf publications from: ")
my_content = urllib2.urlopen(my_url).read()

#print my_soup.prettify()
my_soup = BeautifulSoup(my_content, "lxml")

# find a tag
a_tags = my_soup.findAll('a')
for item in a_tags:

        # get href items
        my_link = item['href']

        if my_link.find('.pdf') != -1:
            file_name = item.contents[0]

            # replace spaces
            file_no_spaces = file_name.replace(" ", "_")

            # replace commas
            file_no_spaces = file_name.replace(",", "_")

            # replace colon
            file_no_spaces = file_name.replace(":", "_")

            # replace semicolon
            file_no_spaces = file_name.replace(";", "_")

            # replace forward slash
            file_replaced = file_no_spaces.replace("/", "-")+'.pdf'

            # download pdf files
            print ("downloading: ", my_link, file_replaced)
            wget.download(my_link, './my-pubs/'+file_replaced)

print('done')

pass

