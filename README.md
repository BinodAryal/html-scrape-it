#  Scrape the single table from html page to csv file #

Code will scrape all the data from single table in given HTML [ page](https://cdn.rawgit.com/younginnovations/internship-challenges/master/data-analysis/scrape-it/exampledata.html) to CSV file containing inside 'out' directory.

##### Requirement:
* Python 2.7.12 +
* BeautifulSoup

To run the script  you need to have ```BeautifulSoup``` installed. You can get it with ```pip install beautifulsoup``` once the BeautifulSoup is installed, install HTML parser with ```pip install lxml```


If you are using ``` python 3 + ``` change ```from urllib2 import urlopen``` in ```run.py``` to ```from urllib import urlopen```

#### Running

 Once the BeautifulSoup and HTML parser  are setup use:
```
git clone https://github.com/BinodAryal/html-scrape-it.git
cd html-scrape-it
python run.py
```
