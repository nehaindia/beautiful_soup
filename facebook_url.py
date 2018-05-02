#!/usr/bin/python2


from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("https://www.facebook.com/")

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    #print(link.get('href'))


print soup.find_all(["a", "b"])

