from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#connects to the page
page = uReq("https://www.billboard.com/charts/hot-100")
html = page.read()
page.close()

#gets the html
page_soup = soup(html,"html.parser")

#opens the file that is being written to
filename = "top 100 songs.csv"
f = open(filename, "w")

#headers for the file
headers = "Song_Name, Artists\n"
f.write(headers)


#splits the page into the 100 songs
containers = page_soup.main.findAll("div",{"class":"chart-row__title"})

#loops through the 100 songs
for container in containers:

    print("Song Title: " + container.contents[1].text+ "\nArtist Name: "+container.contents[3].text.strip()+"\n")

    #replaces the commas in the song name with |
    f.write(container.contents[1].text.replace(",","|")+","+container.contents[3].text.strip()+"\n")

f.close()
