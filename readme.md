## Web Crawler

Given a base url, this script will crawl/scrape all the pages connected to it for a given depth of crawling.
The useful information from the scraped data can be extracted by specifying appropriate regular expressions.

#### Algorithm


###### Crawl

- For a given base url, fetch page html
- Append the new links on this page to pending urls array
- Continue fetching information from links till max depth
- return a mapping of all crawled urls and its data.

###### Fetch
- For each url, push regex match into a results object

