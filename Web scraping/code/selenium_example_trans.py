import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

text = input("To translate: ")

# change Chrome browser language to english
options = webdriver.ChromeOptions()
options.add_argument("--lang=en-GB")
options.add_argument("--headless")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")

driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Chromedriver\chromedriver.exe', options=options)
driver.get("https://www.deepl.com/en/translator")

transInput = driver.find_element_by_xpath('//*[@id="dl_translator"]/div[2]/div[3]/div[2]/div/textarea')
transInput.click()
transInput.send_keys(text)

try:
    loadTrans = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[4]/div[3]/div[1]/textarea')))
    loadTrans.click()
finally:
    time.sleep(8)
    transOutput = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[4]/div[3]/div[2]/p[2]/button[1]')

    print("Translation of: ", text, "\nis: ", transOutput.text)
    driver.quit()
