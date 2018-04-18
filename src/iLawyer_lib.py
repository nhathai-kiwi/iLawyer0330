#!/usr/bin/env python
# -*- coding: utf-8 -*-

# iLawyer library
import iLawyer_basic as ib
import openpyxl
from openpyxl import Workbook

# generate dictionary from xlsx file, keep monosyllable words
# TODO add description for input xlsx
def gen_dict_from_xlsx(inp_xlsx, num_rows, id_column):
    all_questions = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column)
    ib.print_txt_from_array(all_questions, out_txt='vncore_inp.txt') # print output to a file, this file will be deleted later
    ib.process_vncore('vncore_inp.txt', 'vncore_out.txt')
    dict_replicated = ib.gen_words_from_vncore_out_txt('vncore_out.txt')
    dict = ib.gen_distinct_array(dict_replicated)
    dict.sort()
    ib.process_delete_file('vncore_inp.txt')
    ib.process_delete_file('vncore_out.txt')
    return dict, len(dict)
# DONE


# lay tu dien tu file inp_xlsx roi in ra file out_xlsx va out_txt
def print_dict_into_xlsx_and_txt(inp_xlsx, dict_num_rows, id_column_question, out_xlsx, out_txt):
    dict, num_words = gen_dict_from_xlsx(inp_xlsx, dict_num_rows, id_column_question)
    # in ra file .xlsx
    book = Workbook()
    sheet = book.active
    sheet.append(("ID", "Word"))
    id = 0
    for word in dict:
        id += 1
        row =  (id, word)
        sheet.append(row)
    book.save(out_xlsx)

    # in ra file .txt
    fw = open(out_txt, 'w')
    for word in dict:
        fw.write(str(word) + '\n')
    fw.close()

    return 0
# DONE


# generate dictionary from xlsx file, keep multiple syllable words only
def gen_dict_from_xlsx_02(inp_xlsx, num_rows, id_column):
    all_questions = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column)
    ib.print_txt_from_array(all_questions, out_txt='vncore_inp.txt') # print output to a file, this file will be deleted later
    ib.process_vncore('vncore_inp.txt', 'vncore_out.txt')
    dict_replicated = ib.gen_words_from_vncore_out_txt_02('vncore_out.txt')
    dict = ib.gen_distinct_array(dict_replicated)
    dict.sort()
    ib.process_delete_file('vncore_inp.txt')
    ib.process_delete_file('vncore_out.txt')
    return dict, len(dict)
# DONE


# generate dictionary from xlsx file, keep multiple syllable words only
def gen_dict_from_xlsx_with_count(inp_xlsx, num_rows, id_column):
    all_questions = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column)
    ib.print_txt_from_array(all_questions, out_txt='vncore_inp.txt') # print output to a file, this file will be deleted later
    ib.process_vncore('vncore_inp.txt', 'vncore_out.txt')
    dict_replicated = ib.gen_words_from_vncore_out_txt('vncore_out.txt')
    dict = ib.gen_distinct_array_with_count(dict_replicated)
    #dict.sort()
    ib.process_delete_file('vncore_inp.txt')
    ib.process_delete_file('vncore_out.txt')
    return dict, len(dict)
# DONE


# generate feature table and labels from a training set stored in xlsx
# TODO add description for input xlsx
def gen_feature_table_labels(inp_xlsx, num_rows, id_column_question, id_column_label, normal_dict_txt):
    feature_table = ib.gen_feature_table_from_xlsx(inp_xlsx, num_rows, id_column_question, normal_dict_txt)
    labels = ib.gen_column_from_xlsx(inp_xlsx, num_rows, id_column_label)
    return feature_table, labels
