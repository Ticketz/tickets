from selenium import webdriver
import bs4
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup as soup
from selenium.webdriver.firefox.options import Options

def getPrices(browser):
    browser.find_element_by_css_selector('.more.button.button-tertiary.flat').click()
    browser.get(browser.current_url)

    innerHTML = browser.execute_script('return document.body.innerHTML')
    browser.implicitly_wait(3)
    browser.find_element_by_css_selector('.modal-dialog__button.landing-modal-footer__skip-button').click()
    time.sleep(10)
    innerHTML = browser.execute_script('return document.body.innerHTML')

    browser.implicitly_wait(3)
    if(len(soup(innerHTML, 'html.parser').find_all('button', {'class','.modal-dialog__button.landing-modal-footer__skip-button'})) > 0):
        browser.find_element_by_css_selector('.modal-dialog__button.landing-modal-footer__skip-button').click()

    browser.get(browser.current_url)
    browser.find_element_by_css_selector('.zoomer__control--zoomin').click()
    time.sleep(10)
    innerHTML = browser.execute_script('return document.body.innerHTML')
    page_soup = soup(innerHTML, 'html.parser')
    seats = page_soup.find_all('g', {'class', 'seats'})[0]
    print(len(seats.find_all('circle',{'class','seats'})))
    ##print(num_empty_seats)
    return;

options = Options()
options.set_headless(headless=True)
browser = webdriver.Firefox()

browser.get('https://www.ticketmaster.com/search?tm_link=tm_header_search&user_input=migos&q=migos')
getPrices(browser)
browser.close()
