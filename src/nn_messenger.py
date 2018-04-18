#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_basic as ib
from sklearn.externals import joblib
import iLawyer_scikit as isk
input_txt = "input.txt"
# output_txt = "output.txt"

lawInEnterprise_xlsx = 'lawInEnterprise.xlsx'
id_column_content = 2
model = 'iLawyer.pkl'
clf = joblib.load(model)

# kiem tra text co it nhat 2 key_word
def check_text_has_at_least_2_keywords(text):
    ib.print_txt_from_string_element(text, input_txt)
    array_string_question = ib.gen_string_array_from_txt(input_txt)
    if ib.check_question_at_least_2_keywords(array_string_question):
        return True
    return False

# text: cau hoi tu nguoi dung
def get_answer(text):
    ib.print_txt_from_string_element(text, input_txt)
    array_string_question = ib.gen_string_array_from_txt(input_txt)
    # for word in array_string_question:
    #     print word

    answer = ""

    x_question = ib.gen_feature_vector(array_string_question)
    X_question = []
    X_question.append(x_question)
    y_question = isk.gen_prediction(clf, X_question)
    print type(y_question), y_question
    # ib.print_txt_from_prediction(lawInEnterprise_xlsx, y_question[0], id_column_content, output_txt)
    answer = ib.get_article_from_prediction(lawInEnterprise_xlsx, y_question[0], id_column_content)

    # print "Len answer: ", len(answer)
    # Gioi han noi dung tin nhan tra loi <= 2000 ki tu (giao dien messenger cho phep nguoi dung gui tin nhan toi da 2000 ki tu)
    if len(answer) > 2000:
        answer = answer[0:2000]
        # print "Answer: ", ret
    return answer

# get_answer("Thù lao, tiền lương và thưởng của Chủ tịch Hội đồng thành viên, Giám đốc, Tổng giám đốc và người quản lý khác ")