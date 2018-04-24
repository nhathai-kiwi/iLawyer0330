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
import nn_messenger as nnm
default_tree = 'tree_%s'

USER_SEQ = {}
all_message_user_id = {}

def handle_message(event):

    print "Right here we can do anything if we want"
    sender_id = event.sender_id

    print "Even here: ", event

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

    print "Type file: ", type(td)


    if quick_reply:

        # tin nhan nguoi dung gui la quick reply
        quick_reply_payload = quick_reply.get('payload')
        print "String quick: ", quick_reply_payload, type(quick_reply_payload)
        value_payload = int(quick_reply_payload)
        print "HAHA quick: ", value_payload, type(value_payload)

        if value_payload < 100:
            print "Chon ngon ngu"
            lang = quick_reply_payload
            all_message_user_id[sender_id]['lang'] = lang
            page.send(sender_id, td.Tree['100']['text'][lang], td.Tree['100']['quick_reply'])
        elif value_payload == 100:
            # chon loai luat se hoi
            lang = all_message_user_id[sender_id]['lang']
            page.send(sender_id, td.Tree['100']['text'][lang], td.Tree['100']['quick_reply'])

        elif value_payload < 200:
            print "Chon bo luat"
            type_law = quick_reply_payload
            all_message_user_id[sender_id]['type_law'] = type_law
            lang = all_message_user_id[sender_id]['lang']
            # page.send(sender_id, type_law.Node['201']['text'][lang], type_law.Node['201']['quick_reply'])

            # xu li voi tung loai luat
            if type_law == '101':
                page.send(sender_id, tree_101.Node['201']['text'][lang], tree_101.Node['201']['quick_reply'])
            elif type_law == '102':
                page.send(sender_id, tree_102.Node['201']['text'][lang], tree_102.Node['201']['quick_reply'])


        elif value_payload < 1000:
            print "Handle nut trong cay"

            lang = all_message_user_id[sender_id]['lang']
            type_law = all_message_user_id[sender_id]['type_law']

            if type_law == '101':
                page.send(sender_id, tree_101.Node[quick_reply_payload]['text'][lang], tree_101.Node[quick_reply_payload]['quick_reply'])
            elif type_law == '102':
                page.send(sender_id, tree_102.Node[quick_reply_payload]['text'][lang], tree_102.Node[quick_reply_payload]['quick_reply'])

            # page.send(sender_id, type_law.Node[quick_reply_payload]['text'][lang], type_law.Node[quick_reply_payload]['quick_reply'])



        elif value_payload == 1000:
            print "Handle node 1000"
            lang = all_message_user_id[sender_id]['lang']
            page.send(sender_id, td.Tree['1000']['text'][lang])


        elif value_payload == 2001:
            # ket thuc cau hoi
            print "Handle node 2001"
            lang = all_message_user_id[sender_id]['lang']
            page.send(sender_id, td.Tree['2001']['text'][lang])

            del all_message_user_id[sender_id]

        elif value_payload >= 10000:
            # in ra cac dieu luat tuong ung
            print "Handle answer"
            answer = value_payload - 10000
            type_law = all_message_user_id[sender_id]['type_law']
            file_answer = type_law + '.xlsx'
            answer = nnm.get_artilce(file_answer, answer)
            page.send(sender_id, answer)

            # hoi lai nguoi dung
            lang = all_message_user_id[sender_id]['lang']
            print "Lang last: ", lang
            page.send(sender_id, td.Tree['2000']['text'][lang], td.Tree['2000']['quick_reply'][lang])


    else:


        # tin nhan nguoi dung gui la text

        # tin nhan tiep theo cua nguoi dung
        if sender_id in all_message_user_id.keys():

            if 'lang' not in all_message_user_id[sender_id]:
                page.send(sender_id, td.Tree['0']['text'], td.Tree['0']['quick_reply'])
                pass
            else:
                print "Send_id already in dictionary:"

                print "Cau hoi cua nguoi dung: ", message_text
                all_message_user_id[sender_id]['message'].append(message_text)
                type_law = all_message_user_id[sender_id]['type_law']
                model = type_law + '.pkl'
                law_xlsx = type_law + '.xlsx'
                answer = nnm.get_answer_from_text(message_text, model, law_xlsx)
                page.send(sender_id, answer)
                print "Answer = ", answer
                # hoi lai nguoi dung
                lang = all_message_user_id[sender_id]['lang']
                print "Lang last: ", lang
                page.send(sender_id, td.Tree['2000']['text'][lang], td.Tree['2000']['quick_reply'][lang])


        # tin nhan dau tien nguoi dung gui
        else:
            # del all_message_user_id[sender_id]

            print "Here is your first message: ", message_text
            all_message_user_id[sender_id] = {}
            all_message_user_id[sender_id]['first'] = message_text
            all_message_user_id[sender_id]['message'] = []
            page.send(sender_id, td.Tree['0']['text'], td.Tree['0']['quick_reply'])


            # print "First message:"



    # ret_value = {}
    #
    # ret_value['message'] = 'Tuan Nguyen'
    #
    # ret_value['lang'] = '01'
    # ret_value['type_law'] = '101'
    # value = jsonify(ret_value)
    # page.send(sender_id, str(ret_value))

    # page.send(sender_id, td.Tree['0']['text'], td.Tree['0']['quick_reply'], metadata=str(ret_value))
    # page.after_send()