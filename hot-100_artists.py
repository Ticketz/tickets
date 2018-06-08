import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

page = uReq("https://www.billboard.com/charts/hot-100")

page_soup = soup(page.read(),"html.parser")

containers = page_soup.find_all("div",{"class":"chart-row__title"})

f = open("hot-100_artists.csv","w")


for container in containers:
    artists = container.contents[3].text.strip()

    comma_splitter = artists.split(",")
    for artist in comma_splitter:
        and_splitter = artist.split('&')
        for ampersand in and_splitter:
            feature_splitter = ampersand.split("Featuring")
            for feature in feature_splitter:
                x_splitter = feature.split(" x ")
                for x in x_splitter:
                    f.write(x.strip() + ",")
    f.write("\n")
