#!/usr/bin/env python
# -*- coding: utf-8 -*-

# iLawyer library
import sys
from openpyxl import Workbook
from sklearn.externals import joblib
import iLawyer_basic as ib
import iLawyer_scikit as isk

reload(sys)
sys.setdefaultencoding('utf8')


def print_dict_with_law_id(law_id):
    """print tu dien (law, normal) tuong ung voi loai luat: law_id"""
    # lay path den file dict xlsx tuong ung, ten file dict co dinh la dict001.xlsx, dict002.xlsx
    dict001_xlsx = ib.get_path_file_name(law_id, 'dict001.xlsx')
    dict002_xlsx = ib.get_path_file_name(law_id, 'dict002.xlsx')

    # lay so luong moi row cua file dict001.xlsx, dict002.xlsx
    dict001_xlsx_row = ib.NUM_ROWS_DICT[int(law_id) - 101][0]
    dict002_xlsx_row = ib.NUM_ROWS_DICT[int(law_id) - 101][1]

    # lay path den cac file xlsx, txt tuong ung
    basic_dict_txt, basic_dict_xlsx, standard_dict_txt, standard_dict_xlsx = ib.get_path_dict_txt_xlsx(law_id)

    print_dict_into_xlsx_and_txt(inp_xlsx=dict001_xlsx, dict_num_rows=dict001_xlsx_row,
                                 id_column_question=2, out_xlsx=basic_dict_xlsx, out_txt=basic_dict_txt)

    print_dict_into_xlsx_and_txt(inp_xlsx=dict002_xlsx, dict_num_rows=dict002_xlsx_row,
                                 id_column_question=2, out_xlsx=standard_dict_xlsx, out_txt=standard_dict_txt)
    return 0
# DONE


def gen_model_with_law_id(law_id):
    """Tao ra model *.pkl tuong ung voi bo luat law_id"""
    # lay path den file train xlsx tuong ung, ten file train co dinh la train001.xlsx
    train001_xlsx = ib.get_path_file_name(law_id, 'train001.xlsx')
    standard_dict_txt = ib.get_path_file_name(law_id, 'standard_dict.txt')
    train001_xlsx_row = ib.NUM_ROWS_TRAIN[int(law_id) - 101][0]

    X, y = gen_feature_table_labels(inp_xlsx=train001_xlsx, num_rows=train001_xlsx_row,
                                    id_column_question=2, id_column_label=3, standard_dict_txt=standard_dict_txt)
    clf = isk.train_by_MLPClassifier_regularization(X, y, hidden_layer_sizes=213, alpha=0.2, max_iter=400)
    # save model
    model_name = str(law_id) + '.pkl'
    joblib.dump(clf, model_name)

    cal_labels = isk.gen_prediction(clf, X)
    correct_labels = y

    performance = isk.cal_performance(correct_labels, cal_labels)
    print "Performances MLP training set for ", law_id, " : ", performance
    return 0
# DONE


def gen_dict_from_xlsx(inp_xlsx, num_rows, id_column):
    """Generate dictionary from xlsx file, keep monosyllable words"""
    all_questions = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column)
    dict_replicated = ib.gen_string_array_from_text(all_questions)
    dict_array = ib.gen_distinct_array(dict_replicated)
    dict_array.sort()
    return dict_array
# DONE


def gen_feature_table_labels(inp_xlsx, num_rows, id_column_question, id_column_label, standard_dict_txt):
    """Generate feature table and labels from a training set stored in xlsx"""
    feature_table = ib.gen_feature_table_from_xlsx(inp_xlsx, num_rows, id_column_question, standard_dict_txt)
    labels = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column_label)
    return feature_table, labels
# DONE


def print_dict_into_xlsx_and_txt(inp_xlsx, dict_num_rows, id_column_question, out_xlsx, out_txt):
    """Lay tu dien tu file inp_xlsx roi in ra file out_xlsx va out_txt"""
    dict_array = gen_dict_from_xlsx(inp_xlsx, dict_num_rows, id_column_question)
    # in ra file .xlsx
    book = Workbook()
    sheet = book.active
    sheet.append(("ID", "Word"))
    id_word = 0
    for word in dict_array:
        id_word += 1
        row = (id_word, word)
        sheet.append(row)
    book.save(out_xlsx)
    book.close()

    # in ra file .txt
    fw = open(out_txt, 'w')
    for word in dict_array:
        fw.write(str(word) + '\n')
    fw.close()

    return 0
# DONE


def get_answer_from_text(text, type_law, lang, type_text):
    # type_text: o day co 2 dang, 1 ung voi text, 2 ung voi HTML
    model = type_law + '.pkl'
    clf = joblib.load(model)
    law_xlsx = type_law + '.xlsx'
    # lay ra thong tin 2 loai tu dien cua loai luat type_lacolumn
    normal_dict_txt = ib.get_path_file_name(type_law, 'standard_dict.txt')
    law_dict_txt = ib.get_path_file_name(type_law, 'basic_dict.txt')



    # tach cac tu trong text
    string_array = ib.gen_string_array_from_text(text)

    array_answer = []

    if ib.check_string_array_has_profanity(string_array, ib.PROFANITY_TXT):
        array_answer.append(ib.LAW_TREE[0]['profanity_ans']['text'][lang])
    else:
        if ib.check_string_array_has_at_least_2_keywords(string_array, law_dict_txt):
            # ghi nhan duoc cau tra loi
            x_question = ib.gen_feature_vector(string_array, normal_dict_txt)
            X_question = []
            X_question.append(x_question)
            y_question = isk.gen_prediction(clf, X_question)
            id_column = type_text + 1
            array_answer = ib.get_article(type_law, y_question[0], lang, id_column=id_column ) 

        else:
            array_answer.append(ib.LAW_TREE[0]['miss_key_ans']['text'][lang])

    return array_answer