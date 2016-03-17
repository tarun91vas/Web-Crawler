# import modules
import requests
import bs4

# Config Variables
base_url = 'http://localhost:8000/'
start_url = 'page1.html'

# Fetch all links on a page
def get_page_links(url):
    r = requests.get(base_url + start_url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    #print soup.prettify()
    
    links  = soup.find_all('a')
    print links
    return null

# Fetch data on page
def get_page_data():
    return null

# Check if the url is relative or absolute
def is_relative_url(s):
    return null


    












