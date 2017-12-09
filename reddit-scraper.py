from bs4 import BeautifulSoup
import urllib2
import csv
from halo import Halo

csvfile = csv.writer(open('extractdata.csv', 'w'))
csvfile.writerow(["topic", "url"])
pages = int(raw_input("enter number of pages to scrap:"))
url = 'https://www.reddit.com/'
i = 1
while pages > 0:
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0')
    myurlopener = urllib2.build_opener()
    myurl = myurlopener.open(request)
    spinner = Halo(text="Processing Page", spinner="dots")
    spinner.start()
    myurldata = myurl.read()
    soup = BeautifulSoup(myurldata, 'lxml')
    for choice in soup.find_all('div', class_='top-matter'):
        if choice.p.a.get('href').startswith('/r/'):
            csvfile.writerow([choice.p.a.text.encode('utf-8'), 'https://www.reddit.com' + choice.p.a.get('href').encode('utf-8')])
        else:
            csvfile.writerow([choice.p.a.text.encode('utf-8'), choice.p.a.get('href').encode('utf-8')])
    nextUrl = soup.find_all('span', class_='next-button')
    for nurl in nextUrl:
        url = nurl.a.get('href')
    pages = pages - 1
    print "\nPage Number " + str(i) + " complete"
    i = i + 1
print "Scraping Complete"
