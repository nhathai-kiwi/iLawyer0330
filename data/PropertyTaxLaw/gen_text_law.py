#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import time
import os
import openpyxl


# get all link company
def get_all_url_companys(url_base, start, end):
    print "url_base: ", url_base
    links = []
    for i in range(start, end + 1):
        len_page = 0
        while len_page < 1000:
            print "Page number: ", i
            url = url_base % (urllib.quote(str(i)))
            r = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            # print "Len data: ", len(data)
            len_page = len(data)
            for company in soup.find_all('div', attrs={'class': "news-v3 bg-color-white"}):
                link = company.find('a')
                url = 'https://thongtindoanhnghiep.co' + link.get('href')
                links.append(url)
                # print "Link: ", url

    return links
# DONE


def get_info_law(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    # print soup.text
    len_page = len(data)

    print "Len page: ", len_page # 7845
    # for article in soup.find_all('p style='margin-top:6.0pt'><a name="dieu')
    print len( soup.find_all('p', attrs={'style': "margin-top:6.0pt"}) )
    for article in soup.find_all('p', attrs={'style': "margin-top:6.0pt"}):
        print article.text
    # decoded = json.loads(soup.text)
    # print len(decoded['LtsItem'])
    # f = open("city.txt", "w")
    # num_city = len(decoded['LtsItem'])
    # for city in decoded['LtsItem']:
    #     # print city
    #     f.write(str(city['ID'])  + " "+ str(city['TotalDoanhNghiep']) + " " + str(city['SolrID']) + " " + str(city['Title']) + "\n")
    #     # print city['ID'], " ", city['TotalDoanhNghiep'], " ", city['SolrID']
    #     # print "TotalDoanhNghiep: ", city['TotalDoanhNghiep']
    #     # print "SolrID: ", city['SolrID']
    #



url_law_on_land = 'https://thuvienphapluat.vn/van-ban/Bat-dong-san/Luat-dat-dai-2013-215836.aspx'

get_info_law(url_law_on_land)
