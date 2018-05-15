# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import tree_default as td
import tree_101
import tree_102
import tree_103
from server import page
from flask_jsonpify import jsonify
import nn_messenger as nnm
default_tree = 'tree_%s'

USER_SEQ = {}
all_message_user_id = {}


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

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq


    # thong tin user chua co trong dictionary

    if sender_id not in all_message_user_id.keys():
        # if 'lang' not in all_message_user_id[sender_id]:
        #   page.send(sender_id, td.Tree['0']['text'], td.Tree['0']['quick_reply'])
        all_message_user_id[sender_id] = {}
        # hoi nguoi dung lua chon ngon ngu
        page.send(sender_id, td.Tree['0']['text'], td.Tree['0']['quick_reply'])
        all_message_user_id[sender_id]['last_payload'] = -1


    else:

        print "user already in dictionary && print thong tin all_mess_dict"

        for k, v in all_message_user_id.iteritems():
            print k, v

        # last_payload == -1: bat dau tin nhan
        # last_payload == 1000: bat dau dat cau hoi
        # otherwise: cac payload trong tree
        last_payload = all_message_user_id[sender_id]['last_payload']
        quick_reply_payload = ''
        value_payload = 0

        if quick_reply:
            # tin nhan nguoi dung gui la quick reply
            quick_reply_payload = quick_reply.get('payload')
            # print "String quick: ", quick_reply_payload, type(quick_reply_payload)
            value_payload = int(quick_reply_payload)

        print "value_payload: ", value_payload

        # check cac value cua last_payload
        if last_payload == -1:
            print "Last payload - 1"
            # nguoi dung chon xong ngon ngu
            payload_text = get_payload_from_text(message_text, td.Tree['0']['quick_reply'])

            # lay payload tuong ung voi text
            if payload_text != -1:
                lang = payload_text
                all_message_user_id[sender_id]['lang'] = lang
                page.send(sender_id, td.Tree['100']['text'][lang], td.Tree['100']['quick_reply'])
                all_message_user_id[sender_id]['last_payload'] = 100

            else:
                # hoi nguoi dung lua chon ngon ngu
                print "Here add ngon ngu"
                page.send(sender_id, td.Tree['0']['text'], td.Tree['0']['quick_reply'])
                all_message_user_id[sender_id]['last_payload'] = -1

        # dua ra cau tra loi cho nguoi dung
        elif last_payload == 0:
            lang = all_message_user_id[sender_id]['lang']

            # TODO dua ra cau tra loi cho nguoi dung
            # type_law = all_message_user_id[sender_id]['type_law']

            type_law = all_message_user_id[sender_id]['type_law']
            model = type_law + '.pkl'
            law_xlsx = type_law + '.xlsx'
            answer_array = nnm.get_answer_from_text(message_text, type_law)
            for answer in answer_array:
                page.send(sender_id, answer)

            # print "Answer = ", answer
            # page.send(sender_id, "Cau tra loi: " + message_text)

            # hoi lai nguoi dung
            # page.send(sender_id, td.Tree['2000']['text'][lang], td.Tree['2000']['quick_reply'][lang])


            # chuyen den trang thai hoi nguoi dung co tiep tuc dat cau hoi ko
            page.send(sender_id, td.Tree['2000']['text'][lang], td.Tree['2000']['quick_reply'])
            all_message_user_id[sender_id]['last_payload'] = 2000

        # dua ra tin nhan yeu cau nguoi dung nhap cau hoi
        elif last_payload == 1000:
            lang = all_message_user_id[sender_id]['lang']
            page.send(sender_id, td.Tree['1000']['text'][lang])
            all_message_user_id[sender_id]['last_payload'] = 0

        # check xem nguoi dung muon dat cau hoi nua ko
        elif last_payload == 2000:
            print "Last payload: 2000"

            lang = all_message_user_id[sender_id]['lang']

            payload_text = get_payload_from_text(message_text, td.Tree['2000']['quick_reply'])

            payload_num = int(payload_text)

            # text nguoi dung nhap khong trung voi title trong quick_reply
            if payload_num == -1:
                # chuyen den trang thai hoi nguoi dung co tiep tuc dat cau hoi ko
                page.send(sender_id, td.Tree['2000']['text'][lang], td.Tree['2000']['quick_reply'])
                all_message_user_id[sender_id]['last_payload'] = 2000

            # text nguoi dung nhap trung voi title trong quick_reply
            else:
                # xoa du lieu da co cua nguoi dung
                if sender_id in all_message_user_id.keys():
                    del all_message_user_id[sender_id]

                if payload_num == 100:
                    # nguoi dung tiep tuc dat cau hoi
                    all_message_user_id[sender_id] = {}
                    all_message_user_id[sender_id]['lang'] = lang
                    page.send(sender_id, td.Tree['100']['text'][lang], td.Tree['100']['quick_reply'])
                    all_message_user_id[sender_id]['last_payload'] = 100

                elif payload_num == 2001:
                    page.send(sender_id, td.Tree['2001']['text'][lang])

        else:
            print "Cac truong hop trong tree: ", last_payload

            if 'type_law' in all_message_user_id[sender_id].keys():
                lang = all_message_user_id[sender_id]['lang']
                type_law = all_message_user_id[sender_id]['type_law']

                print "Lang: ", lang, "type law: ", type_law

                payload_num = -1
                payload_text = -1
                last_payload = str(last_payload)

                if type_law == '101':
                    payload_text = get_payload_from_text(message_text, tree_101.Node[last_payload]['quick_reply'])
                    payload_num = int(payload_text)
                    print "Pay num, text: ", payload_num, " ", payload_text
                    if payload_num == -1:
                        page.send(sender_id, tree_101.Node[last_payload]['text'][lang],
                              tree_101.Node[last_payload]['quick_reply'])
                    elif payload_num < 1000:
                        page.send(sender_id, tree_101.Node[payload_text]['text'][lang],
                                  tree_101.Node[payload_text]['quick_reply'])
                        all_message_user_id[sender_id]['last_payload'] = payload_text

                if type_law == '102':
                    payload_text = get_payload_from_text(message_text, tree_102.Node[last_payload]['quick_reply'])
                    payload_num = int(payload_text)

                    if payload_num == -1:
                        page.send(sender_id, tree_102.Node[last_payload]['text'][lang],
                                  tree_102.Node[last_payload]['quick_reply'])
                    elif payload_num < 1000:
                        page.send(sender_id, tree_102.Node[payload_text]['text'][lang],
                                  tree_102.Node[payload_text]['quick_reply'])
                        all_message_user_id[sender_id]['last_payload'] = payload_text

                if type_law == '103':
                    payload_text = get_payload_from_text(message_text, tree_103.Node[last_payload]['quick_reply'])
                    payload_num = int(payload_text)

                    if payload_num == -1:
                        page.send(sender_id, tree_103.Node[last_payload]['text'][lang],
                                  tree_103.Node[last_payload]['quick_reply'])
                    elif payload_num < 1000:
                        page.send(sender_id, tree_103.Node[payload_text]['text'][lang],
                                  tree_103.Node[payload_text]['quick_reply'])
                        all_message_user_id[sender_id]['last_payload'] = payload_text


                if payload_num >= 10000:
                    answer = payload_num - 10000
                    lang = all_message_user_id[sender_id]['lang']
                    type_law = all_message_user_id[sender_id]['type_law']

                    file_answer = type_law + '.xlsx'
                    answer_array = nnm.get_artilce(file_answer, answer)
                    for answer in answer_array:
                        page.send(sender_id, answer)
                    print "Hoi nguoi dung tiep tuc dat cau hoi"

                    # chuyen den trang thai hoi nguoi dung co tiep tuc dat cau hoi ko
                    page.send(sender_id, td.Tree['2000']['text'][lang], td.Tree['2000']['quick_reply'])
                    all_message_user_id[sender_id]['last_payload'] = 2000

                    print "Ket thuc cau hoi"

                elif payload_num == 1000:
                    lang = all_message_user_id[sender_id]['lang']
                    # chuyen den trang thai hoi nguoi dung co tiep tuc dat cau hoi ko
                    page.send(sender_id, td.Tree['1000']['text'][lang])
                    all_message_user_id[sender_id]['last_payload'] = 0

            else:
                # check xem nguoi dung hoi bo luat gi
                # lay payload tuong ung voi text

                payload_text = get_payload_from_text(message_text, td.Tree['100']['quick_reply'])

                if payload_text != -1:
                    lang = all_message_user_id[sender_id]['lang']
                    type_law = payload_text
                    all_message_user_id[sender_id]['type_law'] = type_law


                    # NOTE: add them mot bo luat thi add them type vao day, send payload 201 cho nguoi dung
                    if type_law == '101':
                        page.send(sender_id, tree_101.Node['201']['text'][lang], tree_101.Node['201']['quick_reply'])
                    elif type_law == '102':
                        page.send(sender_id, tree_102.Node['201']['text'][lang], tree_102.Node['201']['quick_reply'])
                    elif type_law == '103':
                        page.send(sender_id, tree_103.Node['201']['text'][lang], tree_103.Node['201']['quick_reply'])

                    all_message_user_id[sender_id]['last_payload'] = 201

                # text nguoi dung nhap khong trung voi title trong quick_reply
                else:

                    lang = all_message_user_id[sender_id]['lang']
                    page.send(sender_id, td.Tree['100']['text'][lang], td.Tree['100']['quick_reply'])
                    all_message_user_id[sender_id]['last_payload'] = 100
