#!/usr/bin/python2


import requests
from bs4 import BeautifulSoup
import csv
import re

r = requests.get("https://github.com/")
data = r.text

soup = BeautifulSoup(data)

for tag in soup.find_all(re.compile("^b")):
	print(tag.name)


print soup.find_all('b')

print soup.find_all(["a", "b"])

print r.status_code

print r.text

if "blocked" in r.text:
	print "we've been blocked"

print r.headers.get("content-type", "unknown")

