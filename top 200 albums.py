from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#connects to the page
page = uReq("https://www.billboard.com/charts/billboard-200")
html = page.read()
page.close()

#gets the html
page_soup = soup(html,"html.parser")

#opens the file that is being written to
filename = "top 200 artists.csv"
f = open(filename, "w")

#headers for the file
headers = "Album, Artist\n"
f.write(headers)


#splits the page into the 100 artists
containers = page_soup.main.findAll("div",{"class":"chart-row__title"})

#iterates through the 100 artists
for container in containers:

    print("Album Name: "+container.contents[1].text +" - Artist Name: "+container.contents[3].text.strip())
    f.write(container.contents[1].text.replace(",","")+","+container.contents[3].text.strip()+"\n")

f.close
