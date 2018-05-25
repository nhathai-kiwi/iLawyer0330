import urllib
from bs4 import BeautifulSoup
import requests


# Luat thue tai asn
URL_LAW = 'https://thuvienphapluat.vn/van-ban/Thue-Phi-Le-Phi/Luat-thue-tai-san-379974.aspx'
r = requests.get(URL_LAW)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

fw = open('101.txt', 'w')

for data in soup.find_all('p', attrs={'style': "margin-top:6.0pt"}):
    # print company, "\n\n"
    fw.write(str(data) + '\n\n')
# print soup
