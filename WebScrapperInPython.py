from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = input('enter website URL to start: ')

# opening up connection and downloading the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# searching and selecting all images
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("img")

# create the CSV file with all the images source
filename = "imgsource.csv"
f = open(filename, "w")

header = "URL"
i = 1
for container in containers:

    source = container["src"]
    print ("source: " + source)
    if source[:1] == "/":
        link = "https:" + source
    else:
        link = source
    f.write(link + "\n")
    filename = str(i)
    i = i+1
    try: 
        imagefile = open(filename + ".jpeg", 'wb')
        imagefile.write(uReq(link).read())
    except Exception as e:
        print(e)
    finally:
        imagefile.close()
    
f.close()