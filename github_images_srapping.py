from bs4 import BeautifulSoup
import urllib
import os
import requests


urlData = urllib.urlopen('https://github.com/ashu3205')
data = str(urlData.readlines())
bs = BeautifulSoup(data)

for link in bs.find_all('img'):
	image = link.get("src")
	r2 = requests.get(image)
	image_name = os.path.split(image)[1]
	with open(image_name, "wb") as f:
        	f.write(r2.content)
	#print(image)

#for link in bs.select("img[src^=https]"):
#	lnk = link["src"]
#	print lnk
        


