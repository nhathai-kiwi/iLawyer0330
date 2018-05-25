#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from flask_jsonpify import jsonify
import iLawyer_basic as ib
import iLawyer_lib as il


def get_value_from_node(type_law, lang, node_num):
    """Lay message, quick_reply tuong ung voi node_num"""
    print "Type_law: ", type_law, "Lang: ", lang, "Node num: ", node_num
    message_node = ''
    quick_reply_node = []
    if node_num >= 200 and node_num < 1000:
        # node_num trong nam trong file 101, 102, 103, ....json
        message_node = ib.LAW_TREE[int(type_law) - 100][str(node_num)]['text'][lang]
        quick_reply_node = ib.LAW_TREE[int(type_law) - 100][str(node_num)]['quick_reply']
    else:
        # cur_node nam trong file 100.json, xu li cac truong hop dac biet
        if node_num == 0:
            message_node = ib.LAW_TREE[0]['0']['text']
            quick_reply_node = ib.LAW_TREE[0]['0']['quick_reply']

        elif node_num == 1000 or node_num == 2001:
            message_node = ib.LAW_TREE[0][str(node_num)]['text'][lang]
        else:
            message_node = ib.LAW_TREE[0][str(node_num)]['text'][lang]
            quick_reply_node = ib.LAW_TREE[0][str(node_num)]['quick_reply']

    return message_node, quick_reply_node

def handle_post_request(payload):
    """Xu li tin nhan cua nguoi dung tren google firebase"""

    # lay thong tin nhan duoc tu request
    data = json.loads(payload)
    user_id = data['user_id']
    message = data['message'].lower()
    lang = data['lang']
    type_law = data['type_law']
    cur_node = data['cur_node']

    # thong tin tra ve
    message_ret = {}
    message_ret['user_id']  = user_id
    message_ret['message'] = [] # string_array
    message_ret['quick_reply'] = []
    message_ret['lang']  = lang
    message_ret['type_law'] = type_law
    message_ret['cur_node'] = cur_node


    if cur_node == -1:
        "Gui tin nhan lua chon ngon ngu den nguoi dung"
        message_ret['message'].append(ib.LAW_TREE[0]['0']['text'])
        message_ret['quick_reply'] = ib.LAW_TREE[0]['0']['quick_reply']
        message_ret['cur_node'] = 0
    else:

        if cur_node == 0:
            # luu lai lua chon ngon ngu cua nguoi dung
            payload = ib.get_payload_from_text(message, ib.LAW_TREE[0]['0']['quick_reply'])
            print "Palyload ngon ngu: ", payload
            # set language cua nguoi dung
            if message == 'vietnamese':
                message_ret['lang'] = 'vi'
                lang = 'vi'
            elif message == '日本語':
                message_ret['lang'] = 'ja'
                lang = 'ja'


        elif cur_node == 100:
            # luu lai lua chon luat cua nguoi dung
            print "Chon loai luat"

            payload = ib.get_payload_from_text(message, ib.LAW_TREE[0]['100']['quick_reply'])

            # nguoi dung nhap dung title
            if payload != -1:
                type_law = str( 100 + int(message) )
                message_ret['type_law'] = type_law

        elif cur_node == 1000:
            # lay cau hoi cua nguoi dung va dua ra cau tra loi
            # print "Cau hoi cua nguoi dung: ", message_text
            # page.send(sender_id, "Cau hoi nguoi dung: " + message_text)
            # type_text = 1 tuong ung voi dang text tra ve la text
            # type_text = 2 tuong ung voi dang text tra ve la HTML
            answer_array = il.get_answer_from_text(message, type_law, lang, type_text=2)
            message_ret['message'] = answer_array

            payload = 2000

        else:
            # cac truong hop khac trong cay (deu co quick_reply)
            type_law = int(type_law)
            if cur_node >= 200 and cur_node < 1000:
                payload = ib.get_payload_from_text(message, ib.LAW_TREE[type_law - 100][str(cur_node)]['quick_reply'])
            else:
                payload = ib.get_payload_from_text(message, ib.LAW_TREE[0][str(cur_node)]['quick_reply'])

            print "Payload value: ", payload


        payload = int(payload)

        print "Next node: ", payload, " type law: ", type_law, " TYPE: ", type(type_law), " lang: ", lang

        if payload >= 10000:
            # dua ra dieu luat cho nguoi dung
            # page.send(sender_id, "Cau tra loi day.")
            article_num = payload - 10000
            # id_column = 2 voi Text, id_column = 3 vs HTML
            answer_array = ib.get_article(type_law, article_num, lang, id_column=3)
            message_ret['message'] = answer_array

            payload = 2000

        # Gui tin nhan tiep theo cho nguoi dung dua vao payload
        if payload == -1:
            # nguoi dung nhap sai title, yeu cau nguoi dung nhap lai
            if lang:
                # nguoi dung da chon duoc ngon ngu
                message_ret['message'].append(ib.LAW_TREE[0]['invalid_quick_reply']['text'][lang])
                # page.send(sender_id, ib.LAW_TREE[0]['invalid_quick_reply']['text'][lang])

            message_node, quick_reply_node = get_value_from_node(type_law, lang, cur_node)
            message_ret['message'].append(message_node)
            message_ret['quick_reply'] = quick_reply_node
            message_ret['cur_node'] = cur_node

        else:
            # print "Gui tin nhan tiep theo voi payload: ", payload
            # gui tin nhan tiep theo cho nguoi dung: payload

            message_node, quick_reply_node = get_value_from_node(type_law, lang, payload)
            print "Payload send value: ", payload, " ", message_node, " ", quick_reply_node
            message_ret['message'].append(message_node)
            message_ret['quick_reply'] = quick_reply_node
            message_ret['cur_node'] = payload

        # nguoi dung ket thuc phien hoi, set lai payload = -1
        if payload == 2001:
            message_ret['cur_node'] = -1

    return jsonify(message_ret)