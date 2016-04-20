"""
The MIT License (MIT)

Copyright (c) 2016 Tarun Vashisth

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
import bs4
from urlparse import urljoin
import pprint

class Crawler(object):
        def __init__(self, url, depth):
            self.depth = depth
            self.links = [url]
            self.link_depth_map = {url: 0}
        
        
        def get_clean_url(self, baseurl, s):
            """
            Checks whether url is relative or absolute, returns complete url
            """
            if s.find('http://') > -1 or s.find('https://') > -1:
                return s
            else:
                return urljoin(baseurl, s)
        
        
        def get_page_links(self, url, html_data):
            """
            Returns the no of links origination from page content
            """
            atags  = html_data.find_all('a')
            links = []
            for link in atags:
                link_url = self.get_clean_url(url, link.get('href'))
                links.append(link_url)
            return links
        
        def get_page_data(self, url):
            """
            Fetches the html content of the given url
            """
            r = requests.get(url)
            data = bs4.BeautifulSoup(r.text, 'html.parser')
            return data
        
        def crawl(self):
            """
            Performs the actual crawling and returns scraped data
            """
            result = {}
    
            while self.links:
                link = self.links[0]
                self.links = self.links[1:]
                
                if self.link_depth_map[link] <= self.depth:
                    print 'Fetching data for: '+link+'\n'
                    result[link] = self.get_page_data(link)
                    print 'Fetching links for: '+link+'\n'
                    child_links = self.get_page_links(link, result[link])    
                    
                    # update list of links and link_depth
                    for child in child_links:
                        self.links.append(child)
                        self.link_depth_map[child] = self.link_depth_map[link] + 1
                        
            return result

def main():
        start_url = 'http://localhost:8000/page1.html'
        crawler =  Crawler(start_url, 3)
        data = crawler.crawl()
        pprint.pprint(data)

if __name__ == "__main__":
    main()      
