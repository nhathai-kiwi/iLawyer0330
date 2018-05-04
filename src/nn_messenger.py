#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_basic as ib
from sklearn.externals import joblib
import iLawyer_scikit as isk
import os

# ten file chua tu dien cua cac loai luat, ten file giong nhau nhung nam o folder khac nhau
law_dict_txt = 'law_dict.txt'
normal_dict_txt = 'normal_dict.txt'

# duong link dan den tung file tu dien
# folder luat doanh nghiep
law_dict_enterprise_txt = os.path.join(ib.path_law_in_enterprise, law_dict_txt)
normal_dict_enterprise_txt = os.path.join(ib.path_law_in_enterprise, normal_dict_txt)

# folder luat dat dai
law_dict_land_txt = os.path.join(ib.path_law_on_land, law_dict_txt)
normal_dict_land_txt = os.path.join(ib.path_law_on_land, normal_dict_txt)

# folder luat thue tai san
law_dict_property_tax_txt = os.path.join(ib.path_property_tax_law, law_dict_txt)
normal_dict_property_tax_txt = os.path.join(ib.path_property_tax_law, normal_dict_txt)


input_txt = "input.txt"
# output_txt = "output.txt"

lawInEnterprise_xlsx = os.path.join(ib.path_law_in_enterprise, 'lawInEnterprise.xlsx')
lawOnLand_xlsx = os.path.join(ib.path_law_on_land, 'lawOnLand.xlsx')
propertyTaxLaw_xlsx  = os.path.join(ib.path_property_tax_law, 'PropertyTaxLaw.xlsx')

id_column_content = 2



# kiem tra text co it nhat 2 key_word
def check_text_has_at_least_2_keywords(text):
    ib.print_txt_from_string_element(text, input_txt)
    array_string_question = ib.gen_string_array_from_txt(input_txt)
    if ib.check_question_at_least_2_keywords(array_string_question, law_dict_enterprise_txt):
        return True
    return False
# DONE


# lay dieu luat num_artilce trong file inp_xlsx
def get_artilce(law_xlsx, num_article):
    answer = ib.get_article_from_prediction(law_xlsx, num_article, id_column_content)

    array_answer = []

    len_answer = len(answer)
    for i in range(0, (len_answer + 1499) / 1500):
        value = answer[i * 1500 : (i + 1) * 1500 - 1]
        array_answer.append(value)

    return array_answer
# DONE



# text: cau hoi tu nguoi dung, cau tra loi cho luat doanh nghiep
def get_answer_from_text(text, model, law_xlsx, type_law):
    # model = 'iLawyer_enterprise.pkl'
    clf = joblib.load(model)
    if type_law == '101':
        normal_dict_txt = normal_dict_enterprise_txt
    elif type_law == '102':
        normal_dict_txt = normal_dict_land_txt
    elif type_law == '103':
        normal_dict_txt = normal_dict_property_tax_txt

    ib.print_txt_from_string_element(text, input_txt)
    array_string_question = ib.gen_string_array_from_txt(input_txt)
    x_question = ib.gen_feature_vector(array_string_question, normal_dict_txt)
    X_question = []
    X_question.append(x_question)
    y_question = isk.gen_prediction(clf, X_question)

    # print type(y_question), y_question
    # ib.print_txt_from_prediction(lawInEnterprise_xlsx, y_question[0], id_column_content, output_txt)
    answer = ib.get_article_from_prediction(law_xlsx, y_question[0], id_column_content)

    # print "Len answer: ", len(answer)
    # Gioi han noi dung tin nhan tra loi <= 2000 ki tu (giao dien messenger cho phep nguoi dung gui tin nhan toi da 2000 ki tu)
    if len(answer) > 2000:
        answer = answer[0:2000]
    # 0::1500
    array_answer = []

    len_answer = len(answer)
    for i in range(0, (len_answer + 1499) / 1500):
        value = answer[i * 1500 : (i + 1) * 1500 - 1]
        array_answer.append(value)
        # print "Answer: ", ret
    return answer


# text: cau hoi tu nguoi dung, cau tra loi cho luat dat dai
def get_answer_land(text):
    model = 'iLawyer_land.pkl'
    clf = joblib.load(model)

    ib.print_txt_from_string_element(text, input_txt)
    array_string_question = ib.gen_string_array_from_txt(input_txt)
    x_question = ib.gen_feature_vector(array_string_question, normal_dict_land_txt)
    X_question = []
    X_question.append(x_question)
    y_question = isk.gen_prediction(clf, X_question)
    print type(y_question), y_question
    # ib.print_txt_from_prediction(lawInEnterprise_xlsx, y_question[0], id_column_content, output_txt)
    answer = ib.get_article_from_prediction(lawOnLand_xlsx, y_question[0], id_column_content)

    # print "Len answer: ", len(answer)
    # Gioi han noi dung tin nhan tra loi <= 2000 ki tu (giao dien messenger cho phep nguoi dung gui tin nhan toi da 2000 ki tu)
    if len(answer) > 2000:
        answer = answer[0:2000]
        # print "Answer: ", ret
    return answer


# text: cau hoi tu nguoi dung, cau tra loi cho luat thue tai san
def get_answer_property_tax(text):
    model = '103.pkl'
    clf = joblib.load(model)

    ib.print_txt_from_string_element(text, input_txt)
    array_string_question = ib.gen_string_array_from_txt(input_txt)
    x_question = ib.gen_feature_vector(array_string_question, normal_dict_property_tax_txt)
    X_question = []
    X_question.append(x_question)
    y_question = isk.gen_prediction(clf, X_question)
    print type(y_question), y_question
    # ib.print_txt_from_prediction(lawInEnterprise_xlsx, y_question[0], id_column_content, output_txt)
    answer = ib.get_article_from_prediction(propertyTaxLaw_xlsx, y_question[0], id_column_content)

    # print "Len answer: ", len(answer)
    # Gioi han noi dung tin nhan tra loi <= 2000 ki tu (giao dien messenger cho phep nguoi dung gui tin nhan toi da 2000 ki tu)
    if len(answer) > 2000:
        answer = answer[0:2000]
        # print "Answer: ", ret
    return answer
# print get_answer("Thù lao, tiền lương và thưởng của Chủ tịch Hội đồng thành viên, Giám đốc, Tổng giám đốc và người quản lý khác ")
# print get_answer("Quyền và nghĩa vụ của doanh nghiệp cung ứng các sản phẩm, dịch vụ công ích")
# print get_answer_land('Thẩm quyền giải quyết tranh chấp đất đai')
# print get_answer_property_tax('Thuế tài sản cho tàu bay, du thuyền, ô tô')