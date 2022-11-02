import sys
import requests
from bs4 import BeautifulSoup

link = str(sys.argv[1])

thread = requests.get(link)
src = thread.content
soup = BeautifulSoup(src, features="html.parser")

links = soup.find_all("a")
for link in links:
	if "jpg" in link.text:
		url = "https:" + link.attrs["href"]
		
		filename = url.split('/')[-1]
		r = requests.get(url, allow_redirects=True)
		open(filename, 'wb').write(r.content)
		
	elif "png" in link.text:
		url = "https:" + link.attrs["href"]
		
		filename = url.split('/')[-1]
		r = requests.get(url, allow_redirects=True)
		open(filename, 'wb').write(r.content)
		
	elif "webm" in link.text:
		url = "https:" + link.attrs["href"]
		
		filename = url.split('/')[-1]
		r = requests.get(url, allow_redirects=True)
		open(filename, 'wb').write(r.content)
