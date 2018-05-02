#!/usr/bin/python2

from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.pythonforbeginners.com")

data = r.text

soup = BeautifulSoup(data)

print(soup.get_text())              #Extracting all the text from a page
  
for link in soup.find_all('a'):    #Extracting all the URLs found within a page 'a' tags
	
	print(link.get('href'))


print soup.prettify()


print soup.title.string

print soup.p

