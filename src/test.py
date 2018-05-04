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


def get_payload_from_text(message, quick_reply_array):
    message = message.lower()
    for dict in quick_reply_array:
        title = dict['title'].lower()
        pay_load = dict['payload']
        if message == title:
            return pay_load
    return -1

print "Value: ", get_payload_from_text('日語', td.Tree['0']['quick_reply'])



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