import requests
from bs4 import BeautifulSoup
import re

url='https://en.wikipedia.org/wiki/IPhone'

text=requests.get(url).text.encode('utf-8').decode('ascii','ignore')
soup=BeautifulSoup(text,'lxml')
tables=soup.find('table',class_='wikitable')
rows=tables.find_all('tr')[1:]
for row in rows:
    data=row.find_all(['th','td'])
    try:
        version_text = data[0].a.text.split(' ')[1]
        version = re.sub(r'\D',"",version_text)
        print(data[-1].text)
    except:
        pass