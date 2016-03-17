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


###### Tasks 

- For a given base url, fetch page html/data
- For a given base url, crawl all the pages to the depth d.
- Regex search on crawled data
- Find trending for today/week/month/year.
