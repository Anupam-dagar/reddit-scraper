from bs4 import BeautifulSoup
import urllib2
import csv

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
    myurldata = myurl.read()
    soup = BeautifulSoup(myurldata, 'lxml')
    for choice in soup.find_all('a', class_='choice'):
        if choice.get('href').startswith('https://www.reddit.com/r/'):
            csvfile.writerow([choice.text, choice.get('href')])
        else:
            pass
    nextUrl = soup.find_all('span', class_='next-button')
    for nurl in nextUrl:
        url = nurl.a.get('href')
    pages = pages - 1
    print "page number " + str(i) + " complete."
    i = i + 1
print "Scraping Complete"