from selenium import webdriver

# change Chrome browser language to english
options = webdriver.ChromeOptions()
options.add_argument("--lang=en-GB")

# create driver and connect to website
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Chromedriver\chromedriver.exe', options=options)
driver.get("https://www.google.com/search?q=Weather")

# get data from website
temperature = driver.find_element_by_id("wob_tm")
precipitation = driver.find_element_by_xpath('//*[@id="wob_pp"]')
humidity = driver.find_element_by_xpath('//*[@id="wob_hm"]')

print("Temperature: ", temperature.text, "\nPrecipitation: ", precipitation.text,
      "\nHumidity: ", humidity.text)

driver.quit()
