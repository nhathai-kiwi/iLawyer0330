import urllib
from bs4 import BeautifulSoup
import requests


# Luat doanh nghiep
URL_LAW = 'https://thuvienphapluat.vn/van-ban/Doanh-nghiep/Luat-Doanh-nghiep-2014-259730.aspx'
r = requests.get(URL_LAW)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

fw = open('101.txt', 'w')

for data in soup.find_all('p', attrs={'style': "margin-top:6.0pt"}):
    # print company, "\n\n"
    fw.write(str(data) + '\n\n')
# print soup
