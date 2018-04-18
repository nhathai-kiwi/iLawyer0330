# coding: utf-8
from fbmq import QuickReply

CONFIG = {
    'FACEBOOK_TOKEN': 'EAAGHCApnutgBAJEM1ZCySqjfomsi4OgymsEZC5yVxio7mOF4vWCZCRssmD37WvsqQ3pxFux3Ulcsm68PPJSq58njGNLQgGpZA0ZAOZBX8mGlZBb5srU2GMOkSGXCgIJEMQ2LTzZAlBTCDVjk8tb0t4KCrZBqKKwH6ZCzUu5p0EMSXyi0vDFuNqAZAYP',
    'VERIFY_TOKEN': 'tuan_token',
    'SERVER_URL': 'https://0a40a6a2.ngrok.io'
}

final_answer = 'Đề nghị tư vấn luật sư để có câu trả lời chính xác'

law_in_enterprise_xlsx = 'lawInEnterprise.xlsx'

quick_replies_level_0 = [
    QuickReply(title="Công ty trách nhiệm hữu hạn một thành viên", payload="0_0"),
    QuickReply(title="Công ty trách nhiệm hữu hạn hai thành viên trở lên", payload="0_1"),
    QuickReply(title="Doanh nghiệp nhà nước", payload="0_2"),
    QuickReply(title="Công ty cổ phần", payload="0_3"),
    QuickReply(title="Khác", payload="0_4") # final answer
]

quick_replies_level_0_0 = [
    QuickReply(title="Vốn", payload="0_0_0"),
    QuickReply(title="Chủ sở hữu công ty", payload="0_0_1"),
    QuickReply(title="Khác", payload="0_0_2") # final answer
]

quick_replies_level_0_2 = [
    QuickReply(title="Hội đồng thành viên", payload="0_2_0"),
    QuickReply(title="Kiểm soát viên", payload="0_2_1"),
    QuickReply(title="Khác", payload="0_2_2") # final answer
]

quick_replies_level_0_0_0 = [
    QuickReply(title="Thực hiện góp vốn thành lập công ty", payload="0_0_0_0"), # dieu 74
    QuickReply(title="Thay đổi vốn điều lệ", payload="0_0_0_1"), # dieu 87
    QuickReply(title="Khác", payload="0_0_0_2") # final answer
]

quick_replies_level_0_0_1 = [
    QuickReply(title="Quyền của chủ sở hữu công ty", payload="0_0_1_0"), # dieu 75
    QuickReply(title="Nghĩa vụ của chủ sở hữu công ty", payload="0_0_1_1"), # dieu 76
    QuickReply(title="Thực hiện quyền của chủ sở hữu công ty trong một số trường hợp đặc biệt", payload="0_0_1_2"), # dieu 77
    QuickReply(title="Khác", payload="0_0_1_3") # final answer
]

quick_replies_level_0_2_0 = [
    QuickReply(title="Quyền và nghĩa vụ của Hội đồng thành viên", payload="0_2_0_0"), # dieu 91
    QuickReply(title="Tiêu chuẩn và điều kiện đối với thành viên Hội đồng thành viên", payload="0_2_0_1"), # dieu 92
    QuickReply(title="Quyền và nghĩa vụ của các thành viên khác của Hội đồng thành viên", payload="0_2_0_2"), # dieu 95
    QuickReply(title="Khác", payload="0_2_0_3") # final answer
]

quick_replies_level_0_2_1 = [
    QuickReply(title="Tiêu chuẩn và điều kiện đối với Kiểm soát viên", payload="0_2_1_0"), # dieu 103
    QuickReply(title="Trách nhiệm của Kiểm soát viên", payload="0_2_1_1"), # dieu 106
    QuickReply(title="Miễn nhiệm, cách chức Kiểm soát viên", payload="0_2_1_2"), # dieu 107
    QuickReply(title="Khác", payload="0_2_1_3") # khac
]

quick_replies = [{'title': 'Action', 'payload': 'PICK_ACTION'},
               {'title': 'Comedy', 'payload': 'PICK_COMEDY'}]

button_level_0_2_1 = [
    {'title': 'Tiêu chuẩn và điều kiện đối với Kiểm soát viên', 'payload': '0_2_1_0' },
    {'title': 'Trách nhiệm của Kiểm soát viên', 'payload': '0_2_1_1' },
    {'title': 'Miễn nhiệm, cách chức Kiểm soát viên', 'payload': '0_2_1_2' },
    {'title': 'Khác', 'payload': '0_2_1_3' },
]






