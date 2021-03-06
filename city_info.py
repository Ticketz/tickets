import time
import csv
import requests
from selenium import webdriver
import lxml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

options = Options()
options.set_headless(headless=True)
browser = webdriver.Firefox(firefox_options=options, executable_path=r"C:\Users\kunda\OneDrive\Documents\Python Code\geckodriver.exe")

city = "gaithersburg"
state = "md"
url = "https://www.google.com/"
browser.get(url)
search = browser.find_element_by_name('q')
search.send_keys("population of " + city + " " + state)
search.send_keys(Keys.RETURN)
time.sleep(5)
new_url = browser.current_url
browser.get(new_url)
answer = browser.execute_script( "return document.elementFromPoint(arguments[0], arguments[1]);",250, 250).text
answer = answer.split('(')[0]
print(answer)
browser.quit()
