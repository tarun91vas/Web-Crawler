import Crawler as mycrawler
import pprint

# Base url to start crawling
start_url = 'http://localhost:8000/page1.html'
# Initialze crawler instance for depth 3
crawler =  mycrawler.Crawler(start_url, 3)
# Scrape data
data = crawler.crawl()

pprint.pprint(data)