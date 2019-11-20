import requests
from bs4 import BeautifulSoup

def readFile(url):
	r = requests.get(url, headers={'Connection':'close'})
	text = r.text
	if (text[:7] == 'Tu veux'):
		return
	elif (text[:7] == 'Demande'):
		return
	elif (text[:6] == 'Non ce'):
		return
	elif (text[:8] == 'Toujours'):
		return
	print(text)
	print(url)

def recursive(url):
	r = requests.get(url, headers={'Connection':'close'})
	soup = BeautifulSoup(r.text, 'html.parser')
	for a in soup.find_all('a'):
		href = a.get('href')
		if (href == '../'):
			continue
		elif (href == 'README'):
			readFile(url + 'README')
		else:
			recursive(url + href)

recursive('http://192.168.64.6/.hidden/')
