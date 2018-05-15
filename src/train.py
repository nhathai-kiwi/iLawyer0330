# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_lib as il


##########################
# Part 1: training process
# Part 1.1: pre-processing
# training data being stored in a file named "train*.xlsx" with specific format
# dung file law_dict001.xlsx de check xem moi cau hoi co it nhat 2 tu khoa (dict dc gen ra tu file dict001.xlsx)

# xay dung tu dien cho tung loai luat
# moi loai luat duoc gan mot id
# 101: luat doanh nghiep, 102: luat dat dai, 103: luat thue tai san

for law_id in range(101, 104):
    il.print_dict_with_law_id(law_id)


# 1.2: training
for law_id in range(101, 104):
    il.gen_model_with_law_id(law_id)

#
# # 1.3: post-processing
#


# #########################
# # Part 2: cross evaluation
# # print "Performances MLP cross evaluation: ", performance
#
#
# #########################
# # Part 3: validation, prediction