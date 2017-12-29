from bs4 import BeautifulSoup
import html
import dryscrape
import sys
import time

page = "https://cse.google.com/cse?oe=utf8&ie=utf8&source=uds&q=vendor&start=0&sort=&cx=011658049436509675749:gkuaxghjf5u#gsc.tab=0&gsc.q="
run = True

# get from it stopped
with open("count.txt","r+") as file:
    count = int(file.read())

# add words on search
def addSearchValue(page):
    for i in range(1, len(sys.argv)-1):
        page += str(sys.argv[i]) + "%20"
    page += str(sys.argv[len(sys.argv)-1] + "&gsc.sort=&gsc.page=")
    return page


# main url
originalPage = addSearchValue(page)

# profiles output
profileFile = open("output.txt", "a")

while(run):
    # come back from the pagination that stoped
    with open("count.txt","w+") as file:
        file.write(str(count))


    #open section to run javascript
    session = dryscrape.Session()
    #the main page plis the number counter
    session.visit(originalPage + str(count))
    response = session.body()


    try:
        soup = BeautifulSoup(response,"html.parser")

        mydivs = soup.findAll("div", { "class" : "gs-per-result-labels"})

        #get urls in divs which are the profiles
        for item in mydivs:
            if 'url' in item.attrs:
                profileFile.write(str(item.attrs['url']) + "\n")
    except:
        run = False

    count += 1
