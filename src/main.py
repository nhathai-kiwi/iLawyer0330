# this file contains the whole program and is the only one to run
# the purpose is to build a program that gives suggestion in Law of Enterprises based on user's question

import iLawyer_basic as ib
import iLawyer_scikit as isk
from sklearn.externals import joblib
input_txt = "input.txt"
output_txt = "output.txt"

lawInEnterprise_xlsx = 'lawInEnterprise.xlsx'
id_column_content = 2
# model = 'iLawyer.pkl'
# clf = joblib.load(model)

array_string_question = ib.gen_string_array_from_txt(input_txt)
for word in array_string_question:
    print word

# if ib.check_question_at_least_2_keywords(array_string_question):
#     x_question = ib.gen_feature_vector(array_string_question)
#     X_question = []
#     X_question.append(x_question)
#     y_question = isk.gen_prediction(clf, X_question)
#     print type(y_question), y_question
#     ib.print_txt_from_prediction(lawInEnterprise_xlsx, y_question[0], id_column_content, output_txt)
# else:
#     print "Please retype your question."