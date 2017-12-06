# Reddit Scraper

### Usage:
1. Download the required dependencies.
2. Run reddit-scraper.py  
``` python reddit-scraper.py ```  
3. A new file "extractdata.csv" with the data will be created.

### General Information
1. It will scrap the 'hot' topic by default.
2. It does not use reddit API

### Known Issues:
1. It gets the next page url but on visiting the next page url, only count of post change but not the post, this can be reproduced by priting the 'url' variable and opening it in browser.So it can scrap only one page as of now.

### To-do
1. Fix the next page url issue so that it can scrap multiple pages.
2. Increase more data fields.
3. Visualise and draw observations.

### Dependencies
Built using Python version - 2.7  
1. BeautifulSoup
2. urllib2
3. csv
