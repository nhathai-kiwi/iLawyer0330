#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from googletrans import Translator
import tree_default as td
import json

#
def trans_string_into_ja(origin_string, dest_lang):
    """dich mot string sang ngon ngu dest_lang"""
    translator = Translator()
    # translator.detect(origin_string)  # xac dinh ngon ngu
    return translator.translate(origin_string, dest=dest_lang).text
# DONE

# dich mot array string sang tieng nhat va viet ra file txt
def trans_array_string_into_ja(array_string, out_txt):
    translator = Translator()
    translations = translator.translate(array_string, dest='ja')

    f = open(out_txt, 'w')
    for trans in translations:
        f.write(trans.origin + '\n')
        f.write(trans.text + '\n\n')
    f.close()
# DONE


# dich mot array string sang tieng nhat va viet ra file txt
def trans_file_into_vi(inp_txt, out_txt):
    translator = Translator()
    array_string = []
    fr = open(inp_txt, 'r')
    for word in fr:
        print word[:-1]
        array_string.append(word[:-1])

    translations = translator.translate(array_string, dest='vi')

    fw = open(out_txt, 'w')
    for trans in translations:
        fw.write(trans.origin + '\n')
        fw.write(trans.text + '\n\n')
    fw.close()

# DONE
import iLawyer_basic as ib

print len(ib.LAW_TREE[0])
# for k, v in ib.LAW_TREE[0].iteritems():
#     print k
print ib.LAW_TREE[0]['0']['text']
print ib.LAW_TREE[0]['0']['quick_reply']
print ib.LAW_TREE[0]['profanity_ans']['text']['vi']
