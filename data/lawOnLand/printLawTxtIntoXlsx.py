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


law_on_land_txt = 'law_on_land.txt'
law_on_land_xlsx = 'law_on_land.xlsx'

# only apply for LawInEnterprise.txt
def print_into_xlsx(inp_txt):
    data = ''
    lines = []

    with open(inp_txt, 'r') as myfile:
        for line in myfile:
            # check xem la bat dau cua dieu luat: them # vao cuoi dong, ngan cach dieu luat va noi dung
            if (line[0] == '$'):
                line += '#'
            lines.append(line)

    for line in lines:
        data += line
    articles = data.split('$$$$')

    book = Workbook()
    sheet = book.active

    sheet.append(("STT", "Mã số", "Câu hỏi", "Nội dung", "Trả lời"))
    number = 0
    print len(articles)

    for i in range(1, 213):
        number += 1
        content = articles[i].split('#')

        mainContent = content[0].split('. ')
        mainContent[1]  = mainContent[1].replace(chr(10), '')
        # content[1][len(content[1]) - 1].replace('')
        content[1] = content[1][:-1]
        row = (number, mainContent[0], mainContent[1], content[1], mainContent[0] + ":" + mainContent[1] + "\n" + content[1])
        sheet.append(row)
        # print i, " ", mainContent[0], " ", mainContent[1] , content[1]


    book.save(law_on_land_xlsx)
    return 0
# DONE


if __name__ == "__main__":
    print_into_xlsx(law_on_land_txt)


