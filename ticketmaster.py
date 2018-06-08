from selenium import webdriver
import bs4
from bs4 import BeautifulSoup as soup
from selenium.webdriver.firefox.options import Options

#######test#####
options = Options()
options.set_headless(headless=True)
browser = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\dev\OneDrive\Documents\Python Workspace\geckodriver.exe')

url = "https://www.ticketmaster.com/artist/1480454?tm_link=tm_homeA_header_search"
browser.get(url)
innerHTML = browser.execute_script("return document.body.innerHTML")

f = open("Event_Details.csv","w")
f.write('Venue, City, State, Time\n')

page_soup = soup(innerHTML, "html.parser")
getEventDetails(page_soup = page_soup)

browser.close()


def getEventDetails(page_soup):
    info = page_soup.find_all("div", {"class":"padH10"})
    for event in info:
        children = event.contents
        print(children[0].text.split('-')[0] + "," + children[1].text + "," + children[3].text + "," + children[5] + "\n")
        f.write(children[0].text.split('-')[0] + "," + children[1].text + "," + children[3].text + "," + children[5] + "\n")

    return;
