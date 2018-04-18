# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_lib as il
import iLawyer_scikit as isk
import iLawyer_basic as ib
from sklearn.externals import joblib

import os
# duong dan link thu muc hien tai
path = os.path.dirname(os.path.abspath(__file__))

#########################
# Part 1: training process
# Part 1.1: pre-processing
# training data being stored in a file named "tableTraining.xlsx" with specific format TODO add file descritpion
# dung file law_dict001.xlsx de check xem moi cau hoi co it nhat 2 tu khoa (dict dc gen ra tu file dict001.xlsx)

# # xay dung tu dien
# # luat doanh nghiep
# # tu dien chi gom cac tu trong bo luat dict001.xlsx 214 row
# file_dict_law_enterprise = os.path.join(ib.path_law_in_enterprise, 'dict001.xlsx')
# save_dict_law_enterprise_xlsx = os.path.join(ib.path_law_in_enterprise, 'law_dict.xlsx')
# save_dict_law_enterprise_txt = os.path.join(ib.path_law_in_enterprise, 'law_dict.txt')
# il.print_dict_into_xlsx_and_txt(inp_xlsx=file_dict_law_enterprise, dict_num_rows=214, id_column_question=2, out_xlsx=save_dict_law_enterprise_xlsx, out_txt=save_dict_law_enterprise_txt)
#
# # tu dien gom cac tu trong bo luat + cau hoi crawl dict002.xlsx 372 row
# file_dict_law_enterprise = os.path.join(ib.path_law_in_enterprise, 'dict002.xlsx')
# save_dict_law_enterprise_xlsx = os.path.join(ib.path_law_in_enterprise, 'normal_dict.xlsx')
# save_dict_law_enterprise_txt = os.path.join(ib.path_law_in_enterprise, 'normal_dict.txt')
# il.print_dict_into_xlsx_and_txt(inp_xlsx=file_dict_law_enterprise, dict_num_rows=372, id_column_question=2, out_xlsx=save_dict_law_enterprise_xlsx, out_txt=save_dict_law_enterprise_txt)
#
# # luat dat dai
# # tu dien chi gom cac tu trong bo luat dict001.xlsx 213 row
# file_dict_law_land = os.path.join(ib.path_law_on_land, 'dict001.xlsx')
# save_dict_law_land_xlsx = os.path.join(ib.path_law_on_land, 'law_dict.xlsx')
# save_dict_law_land_txt = os.path.join(ib.path_law_on_land, 'law_dict.txt')
# il.print_dict_into_xlsx_and_txt(inp_xlsx=file_dict_law_land, dict_num_rows=213, id_column_question=2, out_xlsx=save_dict_law_land_xlsx, out_txt=save_dict_law_land_txt)
#
# # tu dien gom cac tu trong bo luat + cau hoi crawl dict002.xlsx 300 row
# file_dict_law_land = os.path.join(ib.path_law_on_land, 'dict002.xlsx')
# save_dict_law_land_xlsx = os.path.join(ib.path_law_on_land, 'normal_dict.xlsx')
# save_dict_law_land_txt = os.path.join(ib.path_law_on_land, 'normal_dict.txt')
# il.print_dict_into_xlsx_and_txt(inp_xlsx=file_dict_law_land, dict_num_rows=300, id_column_question=2, out_xlsx=save_dict_law_land_xlsx, out_txt=save_dict_law_land_txt)




# 1.2: training

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

train_xlsx = 'train001.xlsx'

# training cho luat doanh nghiep
# file train cho luat doanh nghiep gom 372 rows, column_question = 2, colum_lable = 3
training_enterprise_xlsx = os.path.join(ib.path_law_in_enterprise, train_xlsx)
X, y = il.gen_feature_table_labels(inp_xlsx=training_enterprise_xlsx, num_rows=372, id_column_question=2, id_column_label=3, normal_dict_txt=normal_dict_enterprise_txt)
clf = isk.train_by_MLPClassifier_regularization(X, y, hidden_layer_sizes=213, alpha=0.2, max_iter=400)
# save model
joblib.dump(clf, 'iLawyer_enterprise.pkl')
cal_labels = isk.gen_prediction(clf, X)
correct_labels = y
performance = isk.cal_performance(correct_labels, cal_labels)
print "Performances MLP training set for Enterprise: ", performance


# training cho luat dat dai
# file train cho luat dat dai gom 300 rows, column_question = 2, colum_lable = 3
training_land_xlsx = os.path.join(ib.path_law_on_land, train_xlsx)
X, y = il.gen_feature_table_labels(inp_xlsx=training_land_xlsx, num_rows=300, id_column_question=2, id_column_label=3, normal_dict_txt=normal_dict_land_txt)
clf = isk.train_by_MLPClassifier_regularization(X, y, hidden_layer_sizes=212, alpha=0.2, max_iter=400)

# save model
joblib.dump(clf, 'iLawyer_land.pkl')
cal_labels = isk.gen_prediction(clf, X)
correct_labels = y
performance = isk.cal_performance(correct_labels, cal_labels)
print "Performances MLP training set for MLP: ", performance



#
# clf = isk.train_by_MLPClassifier_regularization(X, y, hidden_layer_sizes=(num_features), alpha=0.2, max_iter=400)
# # save model
# joblib.dump(clf, 'iLawyer.pkl')
#

#
# # 1.3: post-processing
# # ask_file_name = "ask001.xlsx"
# # ask_num_rows = 5
# # X = ib.gen_feature_table_from_xlsx(ask_file_name, ask_num_rows, id_column_question, dict)
# # y = isk.gen_prediction(clf, X)
# # # print "Label: ", y
# # print "Label: ", y
# #ib.print_txt_from_prediction('lawInEnterprise.xlsx', y[0], 2, 'output.txt')
#
#
# #########################
# # Part 2: cross evaluation
# # print "Performances MLP cross evaluation: ", performance
#
#
# #########################
# # Part 3: validation, prediction