#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from googletrans import Translator

# dich mot string sang tieng nhat
def trans_string_into_ja(origin_string):
    translator = Translator()
    return translator.translate(origin_string, dest='ja').text
# DONE

# dich mot array string sang tieng nhat va viet ra file txt
def trans_array_string_into_ja(array_string, out_txt):
    translator = Translator()
    translations = translator.translate(array_string, dest='ja')

    f = open(out_txt, 'w')
    for trans in translations:
        f.write(trans.origin + '\n')
        f.write(trans.text + '\n\n')
    f.close()
# DONE

#
# text_trans = trans_string_into_ja('Ngành nghề chính: Xây dựng công trình kỹ thuật dân dụng khác')
#
# string_array = ['Đề nghị tư vấn luật sư để có câu trả lời chính xác']
# string_array.append('bạn muốn hỏi cái gì')
# string_array.append('Công ty trách nhiệm hữu hạn một thành viên')
# string_array.append('Công ty trách nhiệm hữu hạn hai thành viên trở lên')
# string_array.append('Doanh nghiệp nhà nước')
# string_array.append('Công ty cổ phần')
# string_array.append('Kết nối luật sư')
# string_array.append('Vốn')
# string_array.append('Chủ sở hữu công ty')
# string_array.append('Khác')
# string_array.append('Hội đồng thành viên')
# string_array.append('Kiểm soát viên')
# string_array.append('Thực hiện góp vốn thành lập công ty')
# string_array.append('Thay đổi vốn điều lệ')
# string_array.append('Quyền của chủ sở hữu công ty')
# string_array.append('Nghĩa vụ của chủ sở hữu công ty')
# string_array.append('Thực hiện quyền của chủ sở hữu công ty trong một số trường hợp đặc biệt')
# string_array.append('Quyền và nghĩa vụ của Hội đồng thành viên')
# string_array.append('Tiêu chuẩn và điều kiện đối với thành viên Hội đồng thành viên')
# string_array.append('Quyền và nghĩa vụ của các thành viên khác của Hội đồng thành viên')
# string_array.append('Tiêu chuẩn và điều kiện đối với Kiểm soát viên')
# string_array.append('Trách nhiệm của Kiểm soát viên')
# string_array.append('Miễn nhiệm, cách chức Kiểm soát viên')
# string_array.append('Bạn có muốn tiếp tục đặt câu hỏi nữa không')
# string_array.append('Có')
# string_array.append('Không')
# string_array.append('Đề nghị tư vấn luật sư để có câu trả lời chính xác')
# string_array.append('Xin mời bạn đưa ra nội dung câu hỏi')
# string_array.append('Bạn có muốn tiếp tục đặt câu hỏi nữa không')
# string_array.append('Xin lỗi hỏi của bạn đưa ra không đủ dữ diện để chúng tôi tìm câu trả lời')
# string_array.append('Mời bạn đưa ra câu hỏi khác')
#
# trans_array_string_into_ja(string_array, 'trans_ja.txt')
