import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

options = Options()
options.set_headless(headless=True)

browser = webdriver.Firefox(firefox_options=options, executable_path=r"C:\Users\kunda\OneDrive\Documents\Python Code\geckodriver.exe")
city = "philadelphia"
day_of_concert = "Mon"
url = "https://www.google.com/"
browser.get(url)
search = browser.find_element_by_name('q')
search.send_keys(city + " weather")
search.send_keys(Keys.RETURN)
time.sleep(5)
new_url = browser.current_url
browser.get(new_url)
innerHTML = browser.execute_script("return document.body.innerHTML")
soup = BeautifulSoup(innerHTML, 'html.parser')
weather = soup.find_all("div",{"class":"gic"})
weather = weather[1]
for children in weather.contents[0]:
    day = children.contents[0].text
    if day_of_concert == day:
        conditions = children.contents[1].contents[0]
        conditions = conditions.get('alt')
        print(conditions,day)









browser.quit()
