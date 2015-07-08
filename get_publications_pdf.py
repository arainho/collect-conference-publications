#encoding=utf-8
__author__ = 'Andre Rainho '
__email__ = 'arainho.it@gmail.com'

from bs4 import BeautifulSoup
import os, sys
import urllib2
import wget

my_url = raw_input("Enter a website to extract pdf publications from: ")
my_content = urllib2.urlopen(my_url).read()
my_soup = BeautifulSoup(my_content, "lxml")

my_path = "./my-pubs"

# find a tag
a_tags = my_soup.findAll('a')

# check if folder to hold publications exists
# if not create it
if not os.path.exists(my_path):
    os.mkdir(my_path, 0755)

for item in a_tags:

        # get href items
        my_link = item['href']

        if my_link.find('.pdf') != -1:
            file_name = item.contents[0]

            # replace if filename begins with space ou ifen
            if file_name.startswith('-'):
                file_name = file_name.replace("-", "_")
            if file_name.startswith(" "):
                file_name = file_name.replace(" ", "")

            # replace spaces
            file_no_spaces = file_name.replace(" ", "_")

            # replace commas
            file_no_commas = file_no_spaces.replace(",", "_")

            # replace colon
            file_no_colon = file_no_commas.replace(":", "_")

            # replace semicolon
            file_no_semicolon = file_no_colon.replace(";", "_")

            # replace forward slash
            file_no_forward_slash = file_no_semicolon.replace("/", "-")

            # add .pdf extension
            file_replaced = file_no_forward_slash+'.pdf'

            # download pdf files
            print ("downloading: ", my_link, file_replaced)
            wget.download(my_link, './my-pubs/'+file_replaced)

print('done')

pass

