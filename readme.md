## Web Crawler

Given a base url, this script will crawl/scrape all the pages linked to it for a given depth of crawling.
The useful information from the scraped data can be extracted by specifying appropriate regular expressions.

#### Project setup
A sample web has been provided to perform the testing. Files can be served using simple python HTTP Server
```sh
$ cd sample_web
$ python -m SimpleHTTPServer 8000
```
Browse sample on 
`http://localhost:8000/page1.html`

#### Algorithm


###### Crawl

- For a given base url, fetch page html
- Append the new links on this page to pending urls array
- Continue fetching information from links till max depth
- return a mapping of all crawled urls and its data.

###### Fetch
- For each url, push regex match into a results object