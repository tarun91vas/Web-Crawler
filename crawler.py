# import modules
import requests
import bs4
import pprint

# Config Variables
base_url = 'http://localhost:8000/'
start_url = 'page1.html'
depth = 2

# Fetch all links on a page
def get_page_links(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    #print soup.prettify()
    
    atags  = soup.find_all('a')
    links = []
    for link in atags:
        links.append(link.get('href'))
    return links

# Fetch data on page
def get_page_data(url):
    r = requests.get(url)
    data = bs4.BeautifulSoup(r.text, 'html.parser')
    return data

# Generate proper url
def get_clean_url(s):
    if s.find('http://') > -1 or s.find('https://') > -1:
        return s
    else:
        return base_url + s

"""
Crawler funtion

Input:
    - url -> url to startwith
    - depth -> depth of crawling

Output:
    - dictionary ->
    {
        link1 : data1,
        link2 : data2
    }
"""
def crawl(url, end_depth):
    # List of links to be crawled
    links = [url]
    # A map to maintain depth of each link
    link_depth = {url : 0}
    # Reslt dictionary
    result = {}
    
    while links:
        link = links[0]
        links = links[1:]
        
        if link_depth[link] <= end_depth:
            print 'Fetching data for: '+link+'\n'
            result[link] = get_page_data(link)
            print 'Fetching links for: '+link+'\n'
            child_links = get_page_links(link)    
            
            # update list of links and link_depth
            for child in child_links:
                child_url = get_clean_url(child)
                links.append(child_url)
                link_depth[child_url] = link_depth[link] + 1
        
    return result


    


pprint.pprint(crawl(base_url+start_url, 2))









