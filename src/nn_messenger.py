#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_basic as ib
from sklearn.externals import joblib
import os

profanity_txt = 'profanity.txt'

lawInEnterprise_xlsx = os.path.join(ib.PATH_LAW_IN_ENTERPRISE, 'lawInEnterprise.xlsx')
lawOnLand_xlsx = os.path.join(ib.PATH_LAW_ON_LAND, 'lawOnLand.xlsx')
propertyTaxLaw_xlsx  = os.path.join(ib.PATH_PROPERTY_TAX_LAW, 'PropertyTaxLaw.xlsx')

id_column_content = 2

USER_SEQ = {}


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


# check xem tin nhan nguoi dung co chua profanity khong?
def check_text_has_profanity_word(text):
    array_string_question = ib.gen_string_array_from_text(text)
    profanity = ib.gen_array_from_txt(profanity_txt)
    for word in array_string_question:
        if word in profanity:
            print "Xuat hien: ", word
            return True
    return False
# DONE


# text: cau hoi tu nguoi dung, cau tra loi cho loai luat: type_law
def get_answer_from_text(text, type_law):
    model = type_law + '.pkl'
    law_xlsx = type_law + '.xlsx'
    normal_dict_txt = ib.get_path_file_name(type_law, 'normal_dict.txt')
    law_dict_txt = ib.get_path_file_name(type_law, 'law_dict.txt')

    clf = joblib.load(model)

    # tach cac tu trong text
    array_string_question = ib.gen_string_array_from_text(text)

    array_answer = []
    if check_text_has_profanity_word(text):
        array_answer.append("Câu hỏi của bạn chứ nội dung thô tục. Mời bạn thao tác lại.")

    else:
        if check_text_has_at_least_2_keywords(text, law_dict_txt):
            x_question = ib.gen_feature_vector(array_string_question, normal_dict_txt)
            X_question = []
            X_question.append(x_question)
            y_question = isk.gen_prediction(clf, X_question)

            # print type(y_question), y_question
            # ib.print_txt_from_prediction(lawInEnterprise_xlsx, y_question[0], id_column_content, output_txt)
            answer = ib.get_article_from_prediction(law_xlsx, y_question[0], id_column_content)

            # print "Len answer: ", len(answer)
            # tach 1500 ki tu thanh 1 tin nhan cho nguoi dung
            len_answer = len(answer)
            for i in range(0, (len_answer + 1499) / 1500):
                value = answer[ (i * 1500) : ((i + 1) * 1500) ]
                array_answer.append(value)
                # print "Answer: ", ret

        else:
            array_answer.append('Câu hỏi của bạn không đủ dữ liệu để chúng tôi trả lời. Mời bạn thao tác lại.')
    return array_answer
# DONE

# check_text_has_profanity_word('Thuế tài sản cho tàu bay, du thuyền, ô tô acrotomophilia')
