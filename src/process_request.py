# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
import config
from flask_jsonpify import jsonify
import config_web as cw
import nn_messenger as nnm

def process_post_request(payload):
    print "Right here we can do anything if we want"
    data = json.loads(payload)

    # {
    # 	"lang" : "",
    # 	"type" : "0",
    # 	"uid" : "12312314",
    # 	"quick_reply" = "",
    # 	"message" = "",
    # 	"all_message" = ""
    # }

    message = data['message']
    all_message = data['all_message']
    uid = data['uid']
    quick_reply = data['quick_reply']
    lang = data['lang']
    # type de danh dau nguoi dung dang dua ra cau hoi
    # type = 1 nguoi dung dua ra cau hoi, type = 2 ket noi luat su, type = 0 la cac tuy chon khac
    type = data['type']
    answer = data['answer']

    ret_value = {}


    ret_value['message'] = ''

    ret_value['quick_reply'] = []
    ret_value['all_message'] = all_message

    ret_value['uid'] = uid

    ret_value['lang'] = lang
    ret_value['type'] = type
    ret_value['answer'] = answer

    # choose language // Vietnamese or Japanese
    if lang == '':
        # dua ra tin nhan chon language cho nguoi dung
        ret_value['message'] = cw.node_choose_language['text']
        ret_value['all_message'] = ''
        ret_value['quick_reply'] = cw.node_choose_language['quick_reply']
        ret_value['type'] = '0'
    else:
        # nguoi dung chon tieng Viet
        if quick_reply == 'vi':
            ret_value['lang'] = 'vi'
            lang = 'vi'
            ret_value['message'] = cw.node_root['text']['vi']
            ret_value['all_message'] = ''
            ret_value['quick_reply'] = cw.node_root['quick_reply']
            ret_value['type'] = '0'

        # nguoi dung chon tieng Nhat
        if quick_reply == 'ja':
            ret_value['lang'] = 'ja'
            lang = 'ja'
            ret_value['message'] = cw.node_root['text']['ja'] # cw.node_root['text']['ja']
            ret_value['all_message'] = ''
            ret_value['quick_reply'] = cw.node_root['quick_reply']
            ret_value['type'] = '0'

        if quick_reply == '1':
            # 1. Công ty trách nhiệm hữu hạn một thành viên
            print "Cong ty trach nhiem huu han mot thanh vien", " ", lang
            ret_value['message'] = cw.node_1['text'][lang]
            ret_value['quick_reply'] = cw.node_1['quick_reply']
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat
            ret_value['all_message'] += " " + cw.node_root['key_words'][0]['word'][0]
            ret_value['type'] = '0'

        if quick_reply == '3':
            # 3. Doanh nghiệp nhà nước
            ret_value['message'] = cw.node_3['text'][lang]
            ret_value['quick_reply'] = cw.node_3['quick_reply']
            # TODO text xu li bang tieng Viet
            ret_value['all_message'] += cw.node_root['key_words'][2]['word'][0]
            ret_value['type'] = '0'
        if quick_reply == '2':
            # 2. Công ty trách nhiệm hữu hạn hai thành viên trở lên
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1' # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat
            ret_value['all_message'] += " " + cw.node_root['key_words'][1]['word'][0]


        if quick_reply == '4':
            # 4. Công ty cổ phần
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat
            ret_value['all_message'] += " " + cw.node_root['key_words'][3]['word'][0]

        if quick_reply == '5':
            # 5. Kết nối luật sư
            # ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '2'  # yeu cau nguoi dung dua ra cau hoi
            ret_value['message'] = cw.last_message[lang]
            ret_value['all_message'] = ''
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat

        if quick_reply == '1_1':
            # yeu cau nguoi dung dua ra cau hoi:
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat
            ret_value['all_message'] += " " +  cw.node_1['key_words'][0]['word'][0]

        if quick_reply == '1_2':
            # yeu cau nguoi dung dua ra cau hoi:
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat
            ret_value['all_message'] += " " + cw.node_1['key_words'][1]['word'][0]

        if quick_reply == '1_3':
            # yeu cau nguoi dung dua ra cau hoi:
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat


        if quick_reply == '3_1':
            # yeu cau nguoi dung dua ra cau hoi:
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat
            ret_value['all_message'] += " " + cw.node_3['key_words'][0]['word'][0]
        if quick_reply == '3_2':
            # yeu cau nguoi dung dua ra cau hoi:
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat
            ret_value['all_message'] += " " + cw.node_3['key_words'][1]['word'][0]

        if quick_reply == '3_3':
            # yeu cau nguoi dung dua ra cau hoi:
            ret_value['message'] = cw.prefer_question[lang]
            ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi
            # TODO text chi xu li bang tieng Viet, can dc xu li bang ca tieng Nhat

        if quick_reply == 'yes':
            # nguoi dung hoi them cau hoi
            ret_value['message'] = cw.node_root['text'][lang]
            ret_value['quick_reply'] = cw.node_root['quick_reply']
            ret_value['type'] = '0'
        if quick_reply == 'no':
            ret_value['all_message'] = ''
            ret_value['message'] = cw.last_message[lang]
            ret_value['type'] = '0'

        if type == '1':
            # nguoi dung dua ra cau hoi
            question = message + " " + all_message
            # TODO xu li va dua ra cau tra loi, tiep tuc dua ra lua chon nguoi dung co muon hoi ko?
            # check message co it nhat 2 key_word
            check_keyword = nnm.check_text_has_at_least_2_keywords(message)
            print question.encode('utf-8') #, " ", message, " ", all_message, " ", check_keyword
            if check_keyword == True:
                answer = nnm.get_answer(question)
                ret_value['answer'] = answer
                ret_value['all_message'] = ''
                ret_value['type'] = '3'
                ret_value['message'] = cw.node_add_question['text'][lang]
                ret_value['quick_reply'] = cw.node_add_question['quick_reply'][lang]
            else:
                # yeu cau nguoi dung nhap lai cau hoi co chua it nhat 2 keyword
                ret_value['message'] = cw.prefer_question[lang]
                ret_value['type'] = '1'  # yeu cau nguoi dung dua ra cau hoi

        if type == '2':
            # TODO
            # dua ra thong tin luat su ma nguoi dung can
            # print "Tu van luat su"
            ret_value['all_message'] = ''
            ret_value['type'] = '0'
            ret_value['message'] = cw.node_add_question['text'][lang]
            ret_value['quick_reply'] = cw.node_add_question['quick_reply'][lang]

    # choose
    return jsonify(ret_value)

def process_send_message(payload):

    return "OK"