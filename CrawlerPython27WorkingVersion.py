import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://google.com"
urls = [url] # stack of urls to scrape
visited = [url] # historic record of urls

def start_point():
    try:
        htmltext = urllib.urlopen(url).read()
    except:
        print url

    soup = BeautifulSoup(htmltext)

    visited.append(url)

    for tag in soup.findAll("a", href = True):
        tag["href"] = urlparse.urljoin(url,tag["href"])
        if tag["href"] not in urls:
            urls.append(tag["href"])
            print "Adding URL: " + tag["href"]
        else:
            print "Already exists: " + tag["href"]

    print "---------------------------------"
    print urls
    print "---------------------------------"

def my_crawler():
    for u in urls:
        try:
            htmltext = urllib.urlopen(u).read()
        except:
            print u

        soup = BeautifulSoup(htmltext)

        urls.pop(0)
        visited.append(u)

        for tag in soup.findAll("a", href = True):
            tag["href"] = urlparse.urljoin(u,tag["href"])
            if tag["href"] not in urls and tag["href"] not in visited:
                urls.append(tag["href"])
                print ""
                print "Adding URL: " + tag["href"]

start_point()

while 1:
    my_crawler()
