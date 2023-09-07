
# Web Scraping using Scrapy

## Introduction to Scrapy
Scrapy is a powerful and open-source web crawling and web scraping framework written in Python. It is designed for efficiently extracting data from websites and is commonly used for various web scraping projects. Scrapy provides a comprehensive set of tools and libraries for building web spiders that can navigate websites, extract data, and save it in structured formats like JSON, CSV, or databases.

### Installation of Scrapy
```
pip install scrapy
```
### Creating a Scrapy project
```
scrapy startproject project_name
```
### Writing a spider
```
cd project_name
scrapy genspider spider_name example.com

```
### writing Spider code
Inside your spider's Python file (located in the spiders directory), you'll define how to navigate the website and extract data using XPath or CSS selectors.

Basic examples of a Scrapy Spider:
```python
import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["http://example.com"]

    def parse(self, response):
        # Extract data here using XPath or CSS selectors
        title = response.css("h1::text").get()
        yield {"title": title}

```
### Running the spider
```
scrapy crawl myspider

```

## References
1. https://docs.scrapy.org/en/latest/index.html
2. https://scrapy.org/
3. https://github.com/scrapy/scrapy


