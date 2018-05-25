#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import pprint
import re
import codecs

from openpyxl import Workbook


law_txt = '102.txt'
law_xlsx = '102.xlsx'
# law_xlsx = 'property_tax_law.xlsx'

# only apply for LawInEnterprise.txt
def print_into_xlsx(inp_txt):
    data = ''
    lines = []

    with open(inp_txt, 'r') as myfile:
        for line in myfile:
            # check xem la bat dau cua dieu luat: them # vao cuoi dong, ngan cach dieu luat va noi dung
            # if (line[0] == '$'):
            #     line += '#'
            lines.append(line)

    for line in lines:
        data += line
    articles = data.split('$$$$')
    print "Len articles: ", len(articles)

    book = Workbook()
    sheet = book.active

    sheet.append(("STT", "Nội dung"))
    number = 0
    # print len(articles)
    #
    for i in range(1, len(articles)):
        number += 1
        row = (number, articles[i])
        sheet.append(row)
    book.save(law_xlsx)

    #
    #     mainContent = content[0].split('. ')
    #     mainContent[1]  = mainContent[1].replace(chr(10), '')
    #     # content[1][len(content[1]) - 1].replace('')
    #     content[1] = content[1][:-1]
    #     row = (number, mainContent[0], mainContent[1], content[1], mainContent[0] + ":" + mainContent[1] + "\n" + content[1])
    #     sheet.append(row)
    #     # print i, " ", mainContent[0], " ", mainContent[1] , content[1]
    #
    #
    # book.save(law_xlsx)
    return 0
# DONE


if __name__ == "__main__":
    print_into_xlsx(law_txt)


