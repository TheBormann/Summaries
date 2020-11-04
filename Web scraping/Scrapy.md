# Scrapy

The best way to scrape the web with python, is with the Scrapy library. It provides flexibility and is optimized for 
massive data scraping

## How it works
 ![Architecture of the Scrapy framework](./img/Scrapy/scrapy_architecture.png "Architecture of the Scrapy framework")
 1. Spider sends a request to the engine
 2. Engine sends request to the scheduler and waits for next request
 3. Scheduler returns the next request to the engine (Here request are ordered in a specific way)
 4. Engine sends request to the downloader passing it through the Downloader middleware
 5. Downloaded page gets send back to the engine passing through the Downloader middleware
 6. Engine sends response from Downloader to spider passing through the spider Middleware
 7. Spider processes the response and sends it back to the engine passing through the spider middleware
 8. Engine sends processed items to item pipelines, sends request to scheduler and asks for next request.
    In the Item pipelines, items are processed and saved in a db
    
 [more information](https://docs.scrapy.org/en/latest/topics/architecture.html)
 
 ## Create a new Scrapy project
First we need to install the library, we will be using the Anaconda packet manager for that:\
(If terminal doesn't find the conda command, add the Anaconda/Scripts folder to environment variables)
```
conda env create --name environment --file=environment.yml

# if environment already exists
conda env update -f environment.yml -n environment 

# switch to the environment
conda activate environment_name
```
Now create a new Scrapy project
```
scrapy startproject project_name
```
this creates the following project structure
```
project
|- project
|   |- spiders              <- Contains all spiders / web crawler
|   |   |- __init__.py      
|   |- __init__.py 
|   |- items.py             <- declares different items, where data is stored
|   |- middlewares.py       <- add processing between crawling steps
|   |- pipelines.py         <- How to process items and how to store them
|   |- settings.py          <- Settings
|- scrapy.cfg
```
## Create a spider
you can create an spider by simply adding a new python file in the spider folder, or use the following command
```
scrapy genspider name website
```
The Spider should look something like this:
```
import scrapy

class countryIndices(scrapy.Spider):
    name = "country"
    start_urls = [
        "https://www.finanzen.net/indizes/alle"
    ]
    allowed_domains = ["https://www.finanzen.net/indizes"]

    def parse(self, response):
        pass
```
The parse method is where the scraping is defined, but before we define how we should process the data, it's necessary to understand Scrapy items.

## Scrapy items
Why do you need to know about Scrapy items?
* Items can be processed before dumping it into a database
* Each Item can be handled differently
* It is fast when handling with large data

To create an item, open the items.py file and add a new class like this:
```
class ItemName(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
```

Later we will run our finished spider with the following command from the shell:
```
scrapy crawl spider_name  -o file_name.json
```
(without -o file_name.json it will print the results to the console)
Later we will call our spider from another script. This is possible with this code.

Now we got our Item "shell" which must be populated with scraped data. To do this, we need to update our
parse method in our Spider:
```
def parse(self, response):
    # create an Itemloader, which uses the item class
    loader = ItemLoader(item=ItemName(), selector=ElementToScrape)
    # add elements to the item values
    loader.add_xpath("valueName", '/x/path/')
    # return the item
    index_item = loader.load_item()
    yield index_item
```

## Pipelines
After fitting the data into the item we can manipulate the data further with pipelines, reasons are:
* cleaning html
* validating scraped data
* dropping duplicates
* storing scraped data

1. Go to the settings.py and add a pipeline (The number describes the order of the pipelines, small comes earlier and max 1000)
    ```
    # Configure item pipelines
    # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
        'StockIndices.pipelines.StockindicesPipeline': 300,
    }
    ```
2. Now we can add a new pipeline in the pipelines.py file:
```
class PipelineName(object):
    def process_item(self, item, spider):
       item["col"] = item["col"] + 2

        return item 
```
This Pipeline adds 2 to every element in the column "col". This is a pretty simple
example, more complicated is, to save your data to an sql database.
(To use the SQL-connector, "SQLAlchemy>=1.3.6" must be added to the environment)

### Save items to SQL
1. Add link to the sqlite db in to settings.py
    ```
    # SQLite
    CONNECTION_STRING = 'sqlite:///relative/link/data.db'   
    ```
2. Add a models.py in the folder with pipelines.py, in there we are defining how to connect to the db and with tables 
should be created:
    ```
    from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
    from sqlalchemy.orm import relationship
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import (
        Integer, String, Date, DateTime, Float, Boolean, Text)
    from scrapy.utils.project import get_project_settings
    
    Base = declarative_base()


    def db_connect():
        """
        Performs database connection using database settings from settings.py.
        Returns sqlalchemy engine instance
        """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


    def create_table(engine):
        Base.metadata.create_all(engine)

   
    class table1(Base):
        __tablename__ = "table1"

    col1 = Column(String, primary_key=True)
    col2 = Column(String)
    col3 = Column(Float)
    ```
3. Now we can define how to save each item in the table, this is done though the pipelines, so we need to update
pipelines.py:
    ```
    class StockindicesPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)
        logging.info("****SaveQuotePipeline: database connected****")

    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        index = Index()
        index.index = item["col1"][0]
        index.country = item["col2"][0]
        index.last = item["col3"][0]

        try:
            session.add(index)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
    ```
   
## Run Spider outside project
This is more tricky and there are two techniques we can choose from.
If our project is small, we can use the Scrapy library and create a scraping program without the framework:
[Here more about that](https://towardsdatascience.com/how-to-run-scrapy-from-a-script-ff07fd6b792b)
The other way is, to run the crawl command outside the framework project. To accomplish this, we are going to update our
framework as follows: ([based on this post](https://stackoverflow.com/questions/31662797/getting-scrapy-project-settings-when-script-is-outside-of-root-directory/47057488#47057488) )

```
my_project/
    main.py                 # Where we are running scrapy from
    scraper/
        run_scraper.py               #Call from main goes here
        scrapy.cfg                   # deploy configuration file
        scraper/                     # project's Python module, you'll import your code from here
            __init__.py
            items.py                 # project items definition file
            pipelines.py             # project pipelines file
            settings.py              # project settings file
            spiders/                 # a directory where you'll later put your spiders
                __init__.py
                mySpider.py     # Contains the QuotesSpider class
```
The main file:
```
from scraper.run_scraper import Scraper
scraper = Scraper()
scraper.run_spiders()
```
run_scraper.py file:
```
from scraper.scraper.spiders.mySpider import mySpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


class Scraper:
    def __init__(self):
        settings_file_path = 'scraper.scraper.settings' # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        self.spider = mySpider # The spider you want to crawl

    def run_spiders(self):
        self.process.crawl(self.spider)
        self.process.start()  # the script will block here until the crawling is finished
```
And at last, we need to update the settings.py:
```
SPIDER_MODULES = ['scraper.scraper.spiders']
NEWSPIDER_MODULE = 'scraper.scraper.spiders'
```
Now our Framework isn't able to run with the traditional "spider crawl mySpider" command, but if we run the main.py
program our framework will be executed!



## How to run your scraper periodically
* When using the normal Scrapy Framework:
    Scrapyd is the best option
* When using the modified Framework, to be callable from Script:
    **Cron** on linux and **schtasks** for windows
    
# Dynamic Web scraping
This is needed, the data you want to scrape is hidden behind java script functionality, or when the website is completely
based on javascript. In these cases it is necessary to simulate the button presses to trigger the js script.

Because Scarpy can't handle simulating clicks or js scripts it needs help from the Selenium library. 

[A refreshment of Selenium](./Selenium.md)

To use Selenium in Scrapy simply call Selenium methods in the Scrapy spider:

Import the Selenium library in your spider
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector
from selenium import webdriver
```
and use Selenium as usually in the spiders parse function
```
basedir = os.path.dirname(os.path.realpath('__file__'))

 def parse(self, response):

 
        # customize the appearence of the browser
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920x1080")
        
        # scrapes without actually opening a browser
        # chrome_options.add_argument("--headless")
        
        
        chrome_driver_path = os.path.join(basedir, 'chromedriver')
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)

        driver.get('https://website.com')

        # now we can work with js
        driver.execute_script("window.scrollTo(0, 50);")

        # and use scrapy to gather the data
        scrapy_selector = Selector(text = driver.page_source)
        
        search_button = driver.find_element_by_css_selector('input[type="login"]')
        search_button.click()
        driver.quit()

```
## Scrapy middleware
Spider middleware are "hooks" that process response and request.
You need middleware if you need to
* post-process output of spider callbacks - change/add/remove requests or items
* post-process start_requests
* handle spider exceptions
To use Scrapy middleware we need to update the settings.py
```
SPIDER_MIDDLEWARES = {
    'myproject.middlewares.CustomSpiderMiddleware': 543,
}
```
Now you need to create a middleware class with specific methods:
```
class CustomSpiderMiddleware(object):
    def process_spider_input(response, spider):
        pass
    
    def process_spider_output(response, result, spider):
        pass

    def process_spider_exception(response, exception, spider):
        pass

    process_start_requests(start_requests, spider):
        pass

    from_crawler(cls, crawler):
        pass
```
For more information about middleware read [here](https://docs.scrapy.org/en/latest/topics/spider-middleware.html#topics-spider-middleware)

One use case for middleware is to bypass website Restrictions using User-Agent.
An User-Agent shows the website with what type of browser the user is trying to connect to the website.
Some websites could block specific browsers from accessing the website, as well as blocking to many requests from the same
browser. To prevent this we can use Scrapy's User-Agent:
1. add scrapy-user-agents to the python environment (not available in anaconda, use pip)
2. comment the USER_AGENT variable in settings.py out
3. Add the following code to the other middleware in the settings file
    ```
    DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    }
    ```
When you are scraping huge amounts of data from a specific website, they might be blocking your ip-adress because of that.
To prevent this there is a middleware called scrapy-proxies, with uses different ip-adresses for each scrape.
More information is accessible here:
https://github.com/aivarsk/scrapy-proxies

## Scrapy without framework
It is possible to run Scrapy without the actual Scrapy framework. This allows you to run the web-crawler from within another 
script.\
To do this you need to create a CrawlProcess and pass it the spider class. 
```
import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


# run spider
if __name__ == "__main__":
    process = CrawlerProcess({
                "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/60.0.3112.101 Safari/537.36",
                "ROBOTSTXT_OBEY": True
            })
    process.crawl(QuotesSpider)
    process.start()
```

## Scrapyd
Scrapyd is a way to schedule and run Scrapy spiders on your own hardware. An alternative to Scrapyd is
www.scrapinghub.com where everything is already set up and your code only needs to get uploaded.
To use Scrapyd we need to do the following steps:
1. Install scrapyd (not available in Anaconda)
    ```
    pip install scrapyd 
    ```
2. To launch scrapyd, type
    ```
    scraypd
    ```
3. Install the scrapyd client for easy spider setup in Scrapyd
    ```
    pip install git+https://github.com/scrapy/scrapyd-client.git
    ```
4. change the deploy section of the scrapy.cfg file to:
    ```
    [deploy:local]
    # Url must point to the scrapy demon url
    url = http://localhost:6800/
    project = myproject
    ```
5. Deploy spider (local referes to the deploy:local section above)
    ```
     scrapyd-deploy local
    ```
6. Now with the curl command, we can add a spider to Scrapyd
    ```
    curl https://localhost:6800/schedule.json -d project=myproject -d spider=myspider
    ```
7. Stop spider (Job-id is accessabel under the jobs tab on the localhost website)
    ```
    curl http://localhost:6800/cancel.json -d project=myproject -d job=myjobid
    ```
Other endpoints that can be changed, can be found here:
https://scrapyd.readthedocs.io/en/latest/api.html

## Good to know
* When website blocks scraping, you can change the USER-AGENT in the settings like this and often it helps
    ```
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    ```
* When using Anacodna as environment manager:
    + Add /path/Anaconda3/scripts to environment variables
    + if your are using powershell, you need to allow to run bash scripts:
    ```
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    ```
    + export Anaconda environment
    ```
    # linux
    conda env export --no-builds | grep -v "prefix" > environment.yml
    # windows
    conda env export --no-builds | findstr -v "prefix" > environment.yml
    ```
    **It is very important to export the file in UTF-8 format!**
 
## Resources
* https://towardsdatascience.com/a-minimalist-end-to-end-scrapy-tutorial-part-i-11e350bcdec0
* https://docs.scrapy.org/en/latest/
* https://towardsdatascience.com/how-to-run-scrapy-from-a-script-ff07fd6b792b
* https://kirankoduru.github.io/python/running-scrapy-programmatically.html