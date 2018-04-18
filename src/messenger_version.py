# coding: utf-8
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

import openpyxl
from config import CONFIG
import config
from fbmq import Attachment, Template, QuickReply, NotificationType
from facebook_page import page
import nn_messenger as nnm
from test_translator import trans_string_into_ja as tsij

dict_message = {}
USER_SEQ = {}
language_text = ''

def handle_message_v07(event):
    global language_text
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    message = event.message
    quick_reply = message.get("quick_reply")

    seq_id = sender_id + ':' + recipient_id
    seq = message.get("seq", 0)


    print "tuan check text: ", language_text
    check_lang = False

    if quick_reply:
        quick_reply_payload = quick_reply.get('payload')
        if quick_reply_payload == 'vi':
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            language_text = 'vi'

            print "Da nhan duoc lan text: vi"
            check_lang = True
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == 'ja':
            page.send(sender_id, config.node_root['text_ja'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            print "Da nhan duoc lan text: ja"
            language_text = 'ja'
            check_lang = True

            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")


    if language_text == '':
        page.send(sender_id, config.node_choose_language['text'], config.node_choose_language['quick_reply'], metadata="DEVELOPER_DEFINED_METADATA")

    else:
        if language_text == 'vi':
            handle_message_v07_vi(event)
        else:
            handle_message_v07_ja(event)


def handle_message_v07_ja(event):
    global language_text
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    # TODO: add code reply to user
    # page.send(sender_id, "Welcome to Ban buoi.")
    # sender_id = '1654392417987542'

    seq = message.get("seq", 0)
    message_id = message.get("mid")
    app_id = message.get("app_id")
    metadata = message.get("metadata")

    message_text = message.get("text")

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")
    print "Type send_id:", type(sender_id)

    # dict_message[sender_id].append(message_text)

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq

    print "Message text: ", message_text.encode("utf-8")

    check_text_question = False

    if quick_reply:
        quick_reply_payload = quick_reply.get('payload')

        print("quick reply for message %s with payload %s" % (message_id, quick_reply_payload))

        # nut noi bo

        if quick_reply_payload == '1':
            page.send(sender_id, config.node_1['text_ja'], config.node_1['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            # add tin nhan cua nguoi dung vao dict
            dict_message[sender_id].append(config.node_root['key_words'][0]['word'][0])

        if quick_reply_payload == '3':
            page.send(sender_id, config.node_3['text_ja'], config.node_3['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_root['key_words'][2]['word'][0])

        if quick_reply_payload == '1_1':
            # page.send(sender_id, config.node_1_1['text'], config.node_1_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][0]['word'][0])
            page.send(sender_id, config.prefer_question_ja)

        if quick_reply_payload == '1_2':
            # page.send(sender_id, config.node_1_2['text'], config.node_1_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][1]['word'][0])
            page.send(sender_id, config.prefer_question_ja)

        if quick_reply_payload == '3_1':
            # page.send(sender_id, config.node_3_1['text'], config.node_3_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][0]['word'][0])
            page.send(sender_id, config.prefer_question_ja)

        if quick_reply_payload == '3_2':
            # page.send(sender_id, config.node_3_2['text'], config.node_3_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][1]['word'][0])
            page.send(sender_id, config.prefer_question_ja)

        # nut la
        if quick_reply_payload == '2':
            page.send(sender_id, config.prefer_question_ja)
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '4':
            page.send(sender_id, config.prefer_question_ja)
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '5':
            # page.send(sender_id, config.final_answer)
            # page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            # page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
            #          metadata="DEVELOPER_DEFINED_METADATA")
            page.send(sender_id, Template.Buttons("選択してください", [
                Template.ButtonWeb("ウェブサイト", "http://www.kiwi-universe.com/"),
                Template.ButtonPhoneNumber("弁護士に電話する", "+16505551234")
            ]))

            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '1_3':
            page.send(sender_id, config.prefer_question_ja)
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '3_3':
            page.send(sender_id, config.prefer_question_ja)
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        # nguoi dung muon dat cau hoi tiep theo
        if quick_reply_payload == 'yes':
            page.send(sender_id, config.node_root['text_ja'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []
            dict_message[sender_id].append("First")

        # nguoi dung ko thao tac nua xoa danh sach tin nhan cua nguoi dung
        if quick_reply_payload == 'no':
            page.send(sender_id, "上記は iLawyer のアドバイスです。 それでも問題が解決しない場合は、弁護士に電話してください")
            language_text = ''
            if sender_id in dict_message.keys():
                del dict_message[sender_id]

    else:
        # nut goc
        # su dung dictionary luu tin nhan cua tung nguoi dung
        # khoi tao dictionary cua tung nguoi
        # dict_message[sender_id] = []

        # check xem la tin nhan dau tien hay tin nhan cau hoi
        if sender_id in dict_message.keys() and len(dict_message[sender_id]) > 0:
            # tin nhan chua noi dung cau hoi
            # print "Tin nhan chua noi dung cau hoi: ", message_text

            dict_message[sender_id].append(message_text)
            check_text_question = True

        # day la truong hop tin nhan dau tien cua nguoi dung
        else:
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            # print "Tin nhan dau tien cua nguoi dung: ", message_text
            # page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")


    if check_text_question == True:

        question_text = ''
        for text in dict_message[sender_id]:
            question_text += ' ' + text
        check_keyword = nnm.check_text_has_at_least_2_keywords(text)

        # page.send(sender_id, "Cau hoi cua ban la: " + question_text)

        if check_keyword:
            #print "Question text final: ", question_text
            answer = nnm.get_answer(question_text)
            answer = tsij(answer)

        if check_keyword == True:
            page.send(sender_id, answer)

        else:
            page.send(sender_id,
                      "申し訳ありません、お客様のお問い合わせは、回答を見つけるための十分な情報を提供していません.\n別の質問をしてください.")

        page.send(sender_id, config.node_add_question['text_ja'], config.node_add_question['quick_reply_ja'],
                  metadata="DEVELOPER_DEFINED_METADATA")

def handle_message_v07_vi(event):
    global language_text
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    # TODO: add code reply to user
    # page.send(sender_id, "Welcome to Ban buoi.")
    # sender_id = '1654392417987542'

    seq = message.get("seq", 0)
    message_id = message.get("mid")
    app_id = message.get("app_id")
    metadata = message.get("metadata")

    message_text = message.get("text")

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")
    print "Type send_id:", type(sender_id)

    # dict_message[sender_id].append(message_text)

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq

    print "Message text: ", message_text.encode("utf-8")

    check_text_question = False

    if quick_reply:
        quick_reply_payload = quick_reply.get('payload')

        print("quick reply for message %s with payload %s" % (message_id, quick_reply_payload))

        # nut noi bo

        if quick_reply_payload == '1':
            page.send(sender_id, config.node_1['text'], config.node_1['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            # add tin nhan cua nguoi dung vao dict
            dict_message[sender_id].append(config.node_root['key_words'][0]['word'][0])

        if quick_reply_payload == '3':
            page.send(sender_id, config.node_3['text'], config.node_3['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_root['key_words'][2]['word'][0])

        if quick_reply_payload == '1_1':
            # page.send(sender_id, config.node_1_1['text'], config.node_1_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][0]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '1_2':
            # page.send(sender_id, config.node_1_2['text'], config.node_1_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][1]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_1':
            # page.send(sender_id, config.node_3_1['text'], config.node_3_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][0]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_2':
            # page.send(sender_id, config.node_3_2['text'], config.node_3_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][1]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        # nut la
        if quick_reply_payload == '2':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '4':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '5':
            # page.send(sender_id, config.final_answer)
            # page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            # page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
            #          metadata="DEVELOPER_DEFINED_METADATA")
            page.send(sender_id, Template.Buttons("Xin mời lựa chọn", [
                Template.ButtonWeb("Trang web", "http://www.kiwi-universe.com/"),
                Template.ButtonPhoneNumber("Gọi điện cho luật sư", "+16505551234")
            ]))

            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '1_3':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '3_3':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        # nguoi dung muon dat cau hoi tiep theo
        if quick_reply_payload == 'yes':
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []
            dict_message[sender_id].append("First")

        # nguoi dung ko thao tac nua xoa danh sach tin nhan cua nguoi dung
        if quick_reply_payload == 'no':
            page.send(sender_id, "Trên đây là nội dung tư vấn của iLawyer. Nếu còn vướng mắc chưa rõ cần luật sư giải đáp, bạn vui lòng gọi đến ...")
            language_text = ''

            if sender_id in dict_message.keys():
                del dict_message[sender_id]


    else:
        # nut goc
        # su dung dictionary luu tin nhan cua tung nguoi dung
        # khoi tao dictionary cua tung nguoi
        # dict_message[sender_id] = []

        # check xem la tin nhan dau tien hay tin nhan cau hoi
        if sender_id in dict_message.keys() and len(dict_message[sender_id]) > 0:
            # tin nhan chua noi dung cau hoi
            # print "Tin nhan chua noi dung cau hoi: ", message_text

            dict_message[sender_id].append(message_text)
            check_text_question = True

        # day la truong hop tin nhan dau tien cua nguoi dung
        else:
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            # print "Tin nhan dau tien cua nguoi dung: ", message_text
            # page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")

    if check_text_question == True:

        question_text = ''
        for text in dict_message[sender_id]:
            question_text += ' ' + text
        check_keyword = nnm.check_text_has_at_least_2_keywords(text)

        # page.send(sender_id, "Cau hoi cua ban la: " + question_text)

        if check_keyword:
            #print "Question text final: ", question_text
            answer = nnm.get_answer(question_text)

        if check_keyword == True:
            page.send(sender_id, answer)

        else:
            page.send(sender_id,
                      "Xin lỗi câu hỏi của bạn đưa ra không đủ dữ diện để chúng tôi tìm câu trả lời.\nMời bạn đưa ra câu hỏi khác.")

        page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
                  metadata="DEVELOPER_DEFINED_METADATA")


# xu li tin nhan messenger version 02 voi classification
def handle_message_v02(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    # TODO: add code reply to user
    # page.send(sender_id, "Welcome to Ban buoi.")

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
    print "Message text: ", message_text.encode("utf-8")

    answer, check_keyword = nnm.get_answer(message_text)

    if check_keyword == True:
        page.send(sender_id, answer)
    else:
        page.send(sender_id,
                  "Xin lỗi câu hỏi của bạn đưa ra không đủ dữ diện để chúng tôi tìm câu trả lời.\nMời bạn nhập lại câu hỏi.")
    # page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'], metadata="DEVELOPER_DEFINED_METADATA")

    # if message_text:
    #     # define message_text that will send
    #     send_message(sender_id, message_text)
    # elif message_attachments:
    #     page.send(sender_id, "Message with attachment received")

def handle_message_v03(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    # TODO: add code reply to user
    # page.send(sender_id, "Welcome to Ban buoi.")
    # sender_id = '1654392417987542'

    seq = message.get("seq", 0)
    message_id = message.get("mid")
    app_id = message.get("app_id")
    metadata = message.get("metadata")

    message_text = message.get("text")

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")
    print "Type send_id:", type(sender_id)

    # dict_message[sender_id].append(message_text)

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq

    print "Message text: ", message_text.encode("utf-8")

    check_text_question = False

    if quick_reply:
        quick_reply_payload = quick_reply.get('payload')

        print("quick reply for message %s with payload %s" % (message_id, quick_reply_payload))

        # nut noi bo

        if quick_reply_payload == '1':
            page.send(sender_id, config.node_1['text'], config.node_1['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            # add tin nhan cua nguoi dung vao dict
            dict_message[sender_id].append(config.node_root['key_words'][0]['word'][0])

        if quick_reply_payload == '3':
            page.send(sender_id, config.node_3['text'], config.node_3['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_root['key_words'][2]['word'][0])

        if quick_reply_payload == '1_1':
            # page.send(sender_id, config.node_1_1['text'], config.node_1_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][0]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '1_2':
            # page.send(sender_id, config.node_1_2['text'], config.node_1_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][1]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_1':
            # page.send(sender_id, config.node_3_1['text'], config.node_3_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][0]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_2':
            # page.send(sender_id, config.node_3_2['text'], config.node_3_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][1]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        # nut la
        if quick_reply_payload == '2':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '4':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '5':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '1_3':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '3_3':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")



    else:
        # nut goc
        # su dung dictionary luu tin nhan cua tung nguoi dung
        # # khoi tao dictionary cua tung nguoi
        # dict_message[sender_id] = []
        # # check xem la tin nhan dau tien hay tin nhan cau hoi

        if sender_id in dict_message.keys() and len(dict_message[sender_id]) > 0:
            # tin nhan chua noi dung cau hoi
            print "Tin nhan chua noi dung cau hoi: ", message_text
            dict_message[sender_id].append(message_text)
            check_text_question = True


        else:
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            print "Tin nhan dau tien cua nguoi dung: ", message_text.encode("utf-8")
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

    if check_text_question == True:

        question_text = ''
        for text in dict_message[sender_id]:
            question_text += ' ' + text
        print "Question text final: ", question_text.encode("utf-8")

        answer, check_keyword = nnm.get_answer(question_text)

        if check_keyword == True:
            page.send(sender_id, answer)

        else:
            page.send(sender_id,
                      "Xin lỗi hỏi của bạn đưa ra không đủ dữ diện để chúng tôi tìm câu trả lời.\nMời bạn đưa ra câu hỏi khác.")

        if sender_id in dict_message.keys():
            del dict_message[sender_id]

def handle_message_v04(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    # TODO: add code reply to user
    # page.send(sender_id, "Welcome to Ban buoi.")
    # sender_id = '1654392417987542'

    seq = message.get("seq", 0)
    message_id = message.get("mid")
    app_id = message.get("app_id")
    metadata = message.get("metadata")

    message_text = message.get("text")

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")
    print "Type send_id:", type(sender_id)

    # dict_message[sender_id].append(message_text)

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq

    print "Message text: ", message_text.encode("utf-8")

    check_text_question = False

    if quick_reply:
        quick_reply_payload = quick_reply.get('payload')

        print("quick reply for message %s with payload %s" % (message_id, quick_reply_payload))

        # nut noi bo

        if quick_reply_payload == '1':
            page.send(sender_id, config.node_1['text'], config.node_1['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            # add tin nhan cua nguoi dung vao dict
            dict_message[sender_id].append(config.node_root['key_words'][0]['word'][0])

        if quick_reply_payload == '3':
            page.send(sender_id, config.node_3['text'], config.node_3['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_root['key_words'][2]['word'][0])

        if quick_reply_payload == '1_1':
            # page.send(sender_id, config.node_1_1['text'], config.node_1_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][0]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '1_2':
            # page.send(sender_id, config.node_1_2['text'], config.node_1_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][1]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_1':
            # page.send(sender_id, config.node_3_1['text'], config.node_3_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][0]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_2':
            # page.send(sender_id, config.node_3_2['text'], config.node_3_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][1]['word'][0])

            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        # nut la
        if quick_reply_payload == '2':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '4':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '5':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '1_3':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")
        if quick_reply_payload == '3_3':
            # page.send(sender_id, config.final_answer)
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            dict_message[sender_id].append("First")

        # nguoi dung muon dat cau hoi tiep theo
        if quick_reply_payload == 'yes':
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

        # nguoi dung ko thao tac nua xoa danh sach tin nhan cua nguoi dung
        if quick_reply_payload == 'no':
            page.send(sender_id, "Trên đây là nội dung tư vấn của iLawyer. Nếu còn vướng mắc, chưa rõ cần luật sư giải đáp, bạn vui lòng gọi đến ...")

            if sender_id in dict_message.keys():
                del dict_message[sender_id]

    else:
        # nut goc
        # su dung dictionary luu tin nhan cua tung nguoi dung
        # khoi tao dictionary cua tung nguoi
        # dict_message[sender_id] = []

        # check xem la tin nhan dau tien hay tin nhan cau hoi
        if sender_id in dict_message.keys() and len(dict_message[sender_id]) > 0:
            # tin nhan chua noi dung cau hoi
            # print "Tin nhan chua noi dung cau hoi: ", message_text
            dict_message[sender_id].append(message_text)
            check_text_question = True

        # day la truong hop tin nhan dau tien cua nguoi dung
        else:
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            # print "Tin nhan dau tien cua nguoi dung: ", message_text
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

    if check_text_question == True:

        question_text = ''
        for text in dict_message[sender_id]:
            question_text += ' ' + text
        check_keyword = nnm.check_text_has_at_least_2_keywords(text)
        if check_keyword:
            #print "Question text final: ", question_text
            answer = nnm.get_answer(question_text)

        if check_keyword == True:
            page.send(sender_id, answer)

        else:
            page.send(sender_id,
                      "Xin lỗi hỏi của bạn đưa ra không đủ dữ diện để chúng tôi tìm câu trả lời.\nMời bạn đưa ra câu hỏi khác.")

        page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
                  metadata="DEVELOPER_DEFINED_METADATA")

def handle_message_v05(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    # TODO: add code reply to user
    # page.send(sender_id, "Welcome to Ban buoi.")
    # sender_id = '1654392417987542'

    seq = message.get("seq", 0)
    message_id = message.get("mid")
    app_id = message.get("app_id")
    metadata = message.get("metadata")

    message_text = message.get("text")

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")
    print "Type send_id:", type(sender_id)

    # dict_message[sender_id].append(message_text)

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq

    print "Message text: ", message_text.encode("utf-8")

    check_text_question = False

    if quick_reply:
        quick_reply_payload = quick_reply.get('payload')

        print("quick reply for message %s with payload %s" % (message_id, quick_reply_payload))

        # nut noi bo

        if quick_reply_payload == '1':
            page.send(sender_id, config.node_1['text'], config.node_1['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            # add tin nhan cua nguoi dung vao dict
            dict_message[sender_id].append(config.node_root['key_words'][0]['word'][0])

        if quick_reply_payload == '3':
            page.send(sender_id, config.node_3['text'], config.node_3['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_root['key_words'][2]['word'][0])

        if quick_reply_payload == '1_1':
            # page.send(sender_id, config.node_1_1['text'], config.node_1_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][0]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '1_2':
            # page.send(sender_id, config.node_1_2['text'], config.node_1_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][1]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_1':
            # page.send(sender_id, config.node_3_1['text'], config.node_3_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][0]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_2':
            # page.send(sender_id, config.node_3_2['text'], config.node_3_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][1]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        # nut la
        if quick_reply_payload == '2':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id not in dict_message:
                dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '4':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id not in dict_message:
                dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '5':
            page.send(sender_id, config.final_answer)
            # page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            if sender_id not in dict_message:
                dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '1_3':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id not in dict_message:
                dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '3_3':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id not in dict_message:
                dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        # nguoi dung muon dat cau hoi tiep theo
        if quick_reply_payload == 'yes':
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

        # nguoi dung ko thao tac nua xoa danh sach tin nhan cua nguoi dung
        if quick_reply_payload == 'no':
            page.send(sender_id, "Trên đây là nội dung tư vấn của iLawyer. Nếu còn vướng mắc chưa rõ cần luật sư giải đáp, bạn vui lòng gọi đến ...")

            if sender_id in dict_message.keys():
                del dict_message[sender_id]

    else:
        # nut goc
        # su dung dictionary luu tin nhan cua tung nguoi dung
        # khoi tao dictionary cua tung nguoi
        # dict_message[sender_id] = []

        # check xem la tin nhan dau tien hay tin nhan cau hoi
        if sender_id in dict_message.keys() and len(dict_message[sender_id]) > 0:
            # tin nhan chua noi dung cau hoi
            # print "Tin nhan chua noi dung cau hoi: ", message_text

            dict_message[sender_id].append(message_text)
            check_text_question = True

        # day la truong hop tin nhan dau tien cua nguoi dung
        else:
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            # print "Tin nhan dau tien cua nguoi dung: ", message_text
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

    if check_text_question == True:

        question_text = ''
        for text in dict_message[sender_id]:
            question_text += ' ' + text
        check_keyword = nnm.check_text_has_at_least_2_keywords(text)
        if check_keyword:
            #print "Question text final: ", question_text
            answer = nnm.get_answer(question_text)

        if check_keyword == True:
            page.send(sender_id, answer)

        else:
            page.send(sender_id,
                      "Xin lỗi hỏi của bạn đưa ra không đủ dữ diện để chúng tôi tìm câu trả lời.\nMời bạn đưa ra câu hỏi khác.")

        page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
                  metadata="DEVELOPER_DEFINED_METADATA")

def handle_message_v06(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_message = event.timestamp
    message = event.message
    print("Received message for user %s and page %s at %s with message:"
          % (sender_id, recipient_id, time_of_message))
    print(message)

    # TODO: add code reply to user
    # page.send(sender_id, "Welcome to Ban buoi.")
    # sender_id = '1654392417987542'

    seq = message.get("seq", 0)
    message_id = message.get("mid")
    app_id = message.get("app_id")
    metadata = message.get("metadata")

    message_text = message.get("text")

    message_attachments = message.get("attachments")

    quick_reply = message.get("quick_reply")
    print "Type send_id:", type(sender_id)

    # dict_message[sender_id].append(message_text)

    seq_id = sender_id + ':' + recipient_id

    if USER_SEQ.get(seq_id, -1) >= seq:
        print("Ignore duplicated request")
        return None
    else:
        USER_SEQ[seq_id] = seq

    print "Message text: ", message_text.encode("utf-8")

    check_text_question = False

    if quick_reply:
        quick_reply_payload = quick_reply.get('payload')

        print("quick reply for message %s with payload %s" % (message_id, quick_reply_payload))

        # nut noi bo

        if quick_reply_payload == '1':
            page.send(sender_id, config.node_1['text'], config.node_1['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            # add tin nhan cua nguoi dung vao dict
            dict_message[sender_id].append(config.node_root['key_words'][0]['word'][0])

        if quick_reply_payload == '3':
            page.send(sender_id, config.node_3['text'], config.node_3['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_root['key_words'][2]['word'][0])

        if quick_reply_payload == '1_1':
            # page.send(sender_id, config.node_1_1['text'], config.node_1_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][0]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '1_2':
            # page.send(sender_id, config.node_1_2['text'], config.node_1_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_1['key_words'][1]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_1':
            # page.send(sender_id, config.node_3_1['text'], config.node_3_1['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][0]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        if quick_reply_payload == '3_2':
            # page.send(sender_id, config.node_3_2['text'], config.node_3_2['quick_reply'],
            #           metadata="DEVELOPER_DEFINED_METADATA")
            dict_message[sender_id].append(config.node_3['key_words'][1]['word'][0])
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")

        # nut la
        if quick_reply_payload == '2':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '4':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '5':
            # page.send(sender_id, config.final_answer)
            # page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            # page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
            #          metadata="DEVELOPER_DEFINED_METADATA")
            page.send(sender_id, Template.Buttons("Xin mời lựa chọn", [
                Template.ButtonWeb("Trang web", "http://www.kiwi-universe.com/"),
                Template.ButtonPhoneNumber("Gọi điện cho luật sư", "+16505551234")
            ]))

            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        if quick_reply_payload == '1_3':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")
        if quick_reply_payload == '3_3':
            page.send(sender_id, "Xin mời bạn đưa ra nội dung câu hỏi:")
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            dict_message[sender_id].append("First")

        # nguoi dung muon dat cau hoi tiep theo
        if quick_reply_payload == 'yes':
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []
            dict_message[sender_id].append("First")

        # nguoi dung ko thao tac nua xoa danh sach tin nhan cua nguoi dung
        if quick_reply_payload == 'no':
            page.send(sender_id, "Trên đây là nội dung tư vấn của iLawyer. Nếu còn vướng mắc chưa rõ cần luật sư giải đáp, bạn vui lòng gọi đến ...")

            if sender_id in dict_message.keys():
                del dict_message[sender_id]

    else:
        # nut goc
        # su dung dictionary luu tin nhan cua tung nguoi dung
        # khoi tao dictionary cua tung nguoi
        # dict_message[sender_id] = []

        # check xem la tin nhan dau tien hay tin nhan cau hoi
        if sender_id in dict_message.keys() and len(dict_message[sender_id]) > 0:
            # tin nhan chua noi dung cau hoi
            # print "Tin nhan chua noi dung cau hoi: ", message_text

            dict_message[sender_id].append(message_text)
            check_text_question = True

        # day la truong hop tin nhan dau tien cua nguoi dung
        else:
            if sender_id in dict_message.keys():
                del dict_message[sender_id]
            dict_message[sender_id] = []

            # print "Tin nhan dau tien cua nguoi dung: ", message_text
            page.send(sender_id, config.node_root['text'], config.node_root['quick_reply'],
                      metadata="DEVELOPER_DEFINED_METADATA")

    if check_text_question == True:

        question_text = ''
        for text in dict_message[sender_id]:
            question_text += ' ' + text
        check_keyword = nnm.check_text_has_at_least_2_keywords(text)

        # page.send(sender_id, "Cau hoi cua ban la: " + question_text)

        if check_keyword:
            #print "Question text final: ", question_text
            answer = nnm.get_answer(question_text)

        if check_keyword == True:
            page.send(sender_id, answer)

        else:
            page.send(sender_id,
                      "Xin lỗi hỏi của bạn đưa ra không đủ dữ diện để chúng tôi tìm câu trả lời.\nMời bạn đưa ra câu hỏi khác.")

        page.send(sender_id, config.node_add_question['text'], config.node_add_question['quick_reply'],
                  metadata="DEVELOPER_DEFINED_METADATA")