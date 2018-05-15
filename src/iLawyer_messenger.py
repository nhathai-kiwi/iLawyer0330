#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""ILawyer messenger handle"""

import iLawyer_basic as ib
from server import page
from sklearn.externals import joblib
import iLawyer_lib as il
USER_SEQ = {}
user_history = {}

# tra ve payload tuong ung voi title = message trong quick_reply_array
# neu ko ton tai title = message thi gia tri tra ve = -1
def get_payload_from_text(message, quick_reply_array):
    message = message.lower()
    for dict in quick_reply_array:
        title = dict['title'].lower()
        pay_load = dict['payload']
        if message == title:
            return pay_load
    return -1


def send_node_message(sender_id, type_law, lang, node_num):
    print "Send node message: ", type_law, " ", lang, " ", node_num
    lang = str(lang)
    node_num = int(node_num)

    if node_num >= 200 and node_num < 1000:
        # node_num trong nam trong file 101, 102, 103, ....json
        page.send(sender_id, ib.LAW_TREE[int(type_law) - 100][str(node_num)]['text'][lang],
                    ib.LAW_TREE[int(type_law) - 100][str(node_num)]['quick_reply'])
    else:
        # cur_node nam trong file 100.json, xu li cac truong hop dac biet
        if node_num == 0:
            page.send(sender_id, ib.LAW_TREE[0]['0']['text'], ib.LAW_TREE[0]['0']['quick_reply'])
        elif node_num == 1000 or node_num == 2001:
            page.send(sender_id, ib.LAW_TREE[0][str(node_num)]['text'][lang])
        else:
            page.send(sender_id, ib.LAW_TREE[0][str(node_num)]['text'][lang],
                    ib.LAW_TREE[0][str(node_num)]['quick_reply'])


def handle_message(event):

    # print "Right here we can do anything if we want"
    sender_id = event.sender_id

    # print "Even here: ", event

    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message

    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    seq = message.get("seq", 0)
    message_id = message.get("mid")
    app_id = message.get("app_id")
    metadata = message.get("metadata")

    message_text = message.get("text")
    message_text = message_text.lower()

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq

    # thong tin user chua co trong dictionary

    if sender_id not in user_history.keys():
        print "Hoi ngon ngu"
        user_history[sender_id] = {}
        # lua chon ngon ngu
        page.send(sender_id, ib.LAW_TREE[0]['0']['text'], ib.LAW_TREE[0]['0']['quick_reply'])
        user_history[sender_id]['cur_node'] = 0

    else:

        print "Here"
        cur_node = user_history[sender_id]['cur_node']
        payload = -1

        if cur_node == 0:
            # luu lai lua chon ngon ngu cua nguoi dung
            payload = get_payload_from_text(message_text, ib.LAW_TREE[0]['0']['quick_reply'])
            print "Palyload ngon ngu: ", payload
            # set language cua nguoi dung
            if message_text == 'vietnamese':
                user_history[sender_id]['lang'] = 'vi'
            elif message_text == '日本語':
                user_history[sender_id]['lang'] = 'ja'

        elif cur_node == 100:
            # luu lai lua chon luat cua nguoi dung
            print "Chon loai luat"

            payload = get_payload_from_text(message_text, ib.LAW_TREE[0]['100']['quick_reply'])

            # nguoi dung nhap dung title
            if payload != -1:
                type_law = str( 100 + int(message_text) )
                user_history[sender_id]['type_law'] = type_law

        elif cur_node == 1000:
            # lay cau hoi cua nguoi dung va dua ra cau tra loi
            # print "Cau hoi cua nguoi dung: ", message_text

            lang = user_history[sender_id]['lang']
            type_law = user_history[sender_id]['type_law']

            # page.send(sender_id, "Cau hoi nguoi dung: " + message_text)
            answer_array = il.get_answer_from_text(message_text, type_law, lang)
            for answer in answer_array:
                page.send(sender_id, answer)

            payload = 2000

        else:
            # cac truong hop khac trong cay (deu co quick_reply)
            type_law = user_history[sender_id]['type_law']
            type_law = int(type_law)
            if cur_node >= 200 and cur_node < 1000:
                payload = get_payload_from_text(message_text, ib.LAW_TREE[type_law - 100][str(cur_node)]['quick_reply'])
            else:
                payload = get_payload_from_text(message_text, ib.LAW_TREE[0][str(cur_node)]['quick_reply'])



        # get lang, type_law from user_history
        lang = ''
        type_law = ''

        if 'lang' in user_history[sender_id].keys():
            lang = user_history[sender_id]['lang']
        if 'type_law' in user_history[sender_id].keys():
            type_law = user_history[sender_id]['type_law']

        payload = int(payload)

        print "Next node: ", payload, " type law: ", type_law, " lang: ", lang

        if payload >= 10000:
            # dua ra dieu luat cho nguoi dung
            # page.send(sender_id, "Cau tra loi day.")
            article_num = payload - 10000

            answer_array = ib.get_article(type_law, article_num, lang)
            print "Cau tra loi day: ", type_law, " ", article_num, " ", lang
            for answer in answer_array:

                page.send(sender_id, answer)

            payload = 2000

        # Gui tin nhan tiep theo cho nguoi dung dua vao payload
        if payload == -1:
            # nguoi dung nhap sai title, yeu cau nguoi dung nhap lai
            if lang:
                # nguoi dung da chon duoc ngon ngu
                page.send(sender_id, ib.LAW_TREE[0]['invalid_quick_reply']['text'][lang])
            send_node_message(sender_id, type_law, lang, cur_node)

        else:
            # print "Gui tin nhan tiep theo voi payload: ", payload
            # gui tin nhan tiep theo cho nguoi dung: payload
            send_node_message(sender_id, type_law, lang, payload)
            user_history[sender_id]['cur_node'] = payload

        # xoa thong tin cua nguoi dung neu nguoi dung khong hoi nua
        if payload == 2001:

            if sender_id in user_history.keys():
                del user_history[sender_id]




