# import modules
import requests
import bs4


url = 'http://localhost:8000/page1.html'
r = requests.get(url)

#Encode to utf-8 on writing to disk or printing
#print r.text.encode('utf-8')
#print r.text

soup = bs4.BeautifulSoup(r.text, 'html.parser')
#print soup.prettify()

links  = soup.find_all('a')
print links



