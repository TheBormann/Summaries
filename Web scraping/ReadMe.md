# Web-scraping
Here are all information gathered on how to scrape any kind of website with 
the libraries Beautiful soup, Selenium and Scrapy.

### Covered Scrapers

+ [Beautiful soup](./Beautiful_soup.md)
+ [Selenium](./Selenium.md)
+ [Scrapy](./Scrapy.md)

## Summary
Overall **Scrapy** is the best choice, especially if you are creating complex
scraping operations, which require efficiency and low power consumption.
In addition, **Scrapy** is highly flexible and with the scrapy-splash project Scrapy
even has Javascript integration. If your scraping is very simple and every
information you want to extract is accessible without an ajax/pjax request
then **Beautiful soup** is your best bet. Finally if your project is simple and
you need JavaScript support than **Selenium** is the way to go.