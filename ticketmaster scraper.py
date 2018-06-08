from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#connects to the page
page = uReq("https://www.vividseats.com/concerts/elton-john-tickets/elton-john-capital-one-arena-9-21-2597129.html")
html = page.read()
page.close()

#gets the html
page_soup = soup(html,"html.parser")

print(page_soup)

#opens the file that is being written to
filename = "ticketmaster.txt"
f = open(filename, "w")

f.write("")
f.close
