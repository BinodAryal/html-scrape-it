import os
import csv
from bs4 import BeautifulSoup as bs
from urllib2 import urlopen

#inisilization
url = urlopen('https://cdn.rawgit.com/younginnovations/internship-challenges/master/data-analysis/scrape-it/exampledata.html').read()
soup = bs(url,'lxml')

#check for "out" folder and if not exist create
path = ('out')
if not os.path.exists(path):
    os.makedirs(path)

#open csv file and write the content fron html table according to tr and td of html
with open('out/data.csv', 'wb') as f:
    writer = csv.writer(f)
    for tr in soup.find_all('tr'):
        td = tr.find_all('td')
        row = [elem.text.encode('utf-8') for elem in td]
        writer.writerow(row)
    f.close()
