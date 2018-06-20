import time
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

options = Options()
options.set_headless(headless=True)
browser = webdriver.Firefox(firefox_options=options, executable_path=r"C:\Users\noahg\AppData\Local\atom\app-1.27.1\geckodriver.exe")

artist = "drake"
birthplace = "birthplace of "+artist


url = "https://www.google.com/"
browser.get(url)


search = browser.find_element_by_name('q')
search.send_keys(birthplace)
search.send_keys(Keys.RETURN)
time.sleep(2)
new_url = browser.current_url
page = requests.get(new_url)
content = page.content
innerHTML = browser.execute_script("return document.body.innerHTML")
#print(innerHTML.decode("utf-8","ignore"),"Html")
soup = BeautifulSoup(innerHTML, 'html.parser')
#soup = BeautifulSoup(content.decode("utf-8",'ignore'),'html.parser')
print(soup.decode("utf-8","ignore"))

#city = soup.find("div",{"class":"Z0LcW"})
city = soup.find("div",{"id":"main"})

print(city)


browser.quit()
