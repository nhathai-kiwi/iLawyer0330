# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import tree_default as td
import tree_101
import tree_102
from flask_jsonpify import jsonify
from facebook_page import page

file_name = tree_101

print tree_101.Node




# node_root = {
#     'key_words': [
#         {'title': '1', 'word': ['cong ty', 'co phan'] },
#         {'title': '2', 'word': ['mot thanh vien', 'hai thanh vien']},
#         {'title': '3', 'word': [] },
#         {'title': '4', 'word': [] },
#         {'title': '5', 'word': [] }
#     ]
# }
# # print len(node_root['key_words'])," ", type(node_root['key_words'])
# # print node_root['key_words'][0]['word']
# dict_main = {}
# tuan = 'String'
# message = ['tuan01', 'tuan02', 'tuan03', 'tuan04']
# msg = 'tuan'
# dict_main['String'] = []
# dict_main[tuan].append(msg)
# dict_main[tuan].append(message)
# # .append(message)
#
# print dict_main['String']
#
# dict = {'Age': 7};
# dict['Name'] = []
# print "Diuct name: ", len(dict['Name'])
# dict['Name'].append('tuan nguyen')
# print "Start Len : %d" %  len(dict)
# # dict.clear()
#
#
# dict['Name'].append('1')
# dict['Name'].append('3')
# dict['Name'].append('2')
#
# for i in dict['Name']:
#     print i=
#
lang = 'ja'
import config_web as cw
print cw.node_1['text'][lang]