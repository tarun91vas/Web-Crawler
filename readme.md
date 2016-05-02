## Web Crawler
Crawler class scrapes the data from the start url until given depth of traversal. It returns a dictionary of crawled url as key and its html content as value. This class can be used as a starter for creating search applications or any other analytics project.

###### Working:
Given a base url, it will crawl/scrape all the pages linked to it for a given depth of crawling.The useful information from the scraped data can be extracted by specifying appropriate regular expressions.

#### Project setup
A sample web has been provided for the proof of concept and testing. Sample web consists of combination of relative and absolute urls along with loops in the web. Crawler class has been tested on above such commonly encountered scenarios of the web. Files can be served using simple python HTTP Server

```sh
$ cd sample_web
$ python -m SimpleHTTPServer 8000
```

Browse sample web on 
`http://localhost:8000/page1.html`

> **Warning:**
> Sample web is no way near to the scenarios and content one will encounter on real web. This is just a starter project and can be extended to suit specific requirements.

###### Test run

```sh
$ python example.py
```
    
`or`

```sh
$ python Crawler.py
```

#### Usage

The code on class usage has been provided in the file `example.py` . 

- Import Crawler class

```sh
    import Crawler as mycrawler
```

 - Set a base url to start crawling
 
 ```sh
    start_url = 'http://localhost:8000/page1.html'
```

 - Initialize the crawler object
 
 ```sh
    crawler =  mycrawler.Crawler(start_url, 3)
```
**NOTE:** First argument is the `base url` and second is the `depth of crawling` which is not same as the number of links crawled but is the graph depth from base url. Depending on how dense is the part of web you want to crawl, choose depth of crawling appropriately.

 - Perform crawling
 
 ```sh
    data = crawler.crawl()
```

 - Sample output is given below
 
 ```sh
    {
        'link1': 'html content for link 1',
        'link2': 'html content for link 2',
        .
        .
        .
    }
```

