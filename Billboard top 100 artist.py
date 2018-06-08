from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


page = uReq("https://www.billboard.com/charts/artist-100")

html = page.read()
page.close()
page_soup = soup(html,"html.parser")

#opens the file that is being written to
filename = "top 100 artists.csv"
f = open(filename, "w")

#headers for the file
headers = "Artists\n"
f.write(headers)


#splits the page into the 100 artists
containers = page_soup.main.findAll("div",{"class":"chart-row__container"})

#iterates through the 100 artists
for container in containers:

    print(container.contents[1].text.strip())

    #writes the artist to the file
    f.write(container.contents[1].text.strip()+"\n")

f.close
