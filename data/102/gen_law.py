import urllib
from bs4 import BeautifulSoup
import requests


# Luat dat dai
URL_LAW = 'https://thuvienphapluat.vn/van-ban/Bat-dong-san/Luat-dat-dai-2013-215836.aspx'
r = requests.get(URL_LAW)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

fw = open('102.txt', 'w')

for data in soup.find_all('p'):
    fw.write(str(data) + '\n\n')

