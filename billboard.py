import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://www.billboard.com/charts/hot-100')
soup = BeautifulSoup(page.text, 'html.parser')

f = open('top-artists.csv', 'w')
artist_name_list = soup.find_all("div", {"class":"chart-row__title"})

for artist_name in artist_name_list:
    artist = artist_name.contents[3].text.strip()

    comma_splitter = artist.split(",")
    for artist in comma_splitter:
        and_splitter =artist.split("&")
        for ampersand in and_splitter:
            feature_splitter = ampersand.split("Featuring")
            for feature in feature_splitter:
                x_splitter = feature.split(" x ")
                for x in x_splitter:
                    f.write(x.strip() + "," )
    f.write("\n")
