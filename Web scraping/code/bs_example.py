import requests
from bs4 import BeautifulSoup
import lxml

# Change appearance of the request
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT,
           "Accept-Language": "en,en-gb;q=0.5"}

# get page
url = "https://www.google.com/search?q=Weather"
result = requests.get(url, headers=headers)

soup = BeautifulSoup(result.content, "lxml")

# scrape website
temperature = soup.find_all("span", {"id": "wob_tm"})
precipitation = soup.find_all("span", {"id": "wob_pp"})
humidity = soup.find_all("span", {"id": "wob_hm"})

print("Temperature: ", temperature[0].getText(), "\nPrecipitation: ", precipitation[0].getText(),
      "\nHumidity: ", humidity[0].getText())
