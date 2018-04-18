# coding: utf-8
from fbmq import QuickReply

CONFIG = {
    'FACEBOOK_TOKEN': 'EAAGHCApnutgBAE4OIGZAh2diLdXNxZA36DmohVZBJhZCGkulcCPMX0Efc1HetuTk4WBDcWZBZCT9m3vskkaTPJordfEs51LcJnkh5t9HCPlJQafnmfchPf8lP53FZADOJZAglm11WA4jpPE3RZAeaaqlFaRChZCDbeZAPchhDd8ZCZA9PPT28MXcOGTyN',
    'VERIFY_TOKEN': 'kiwi_token',
    'SERVER_URL': 'https://3f0390a1.ngrok.io'
}

final_answer = 'Đề nghị tư vấn luật sư để có câu trả lời chính xác'
law_in_enterprise_xlsx = 'lawInEnterprise.xlsx'

node_root = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Công ty trách nhiệm hữu hạn một thành viên\n'
            '2. Công ty trách nhiệm hữu hạn hai thành viên trở lên\n'
            '3. Doanh nghiệp nhà nước\n'
            '4. Công ty cổ phần\n'
            '5. Khác',
    'quick_reply': [
        {'title': '1', 'payload': '1' },
        {'title': '2', 'payload': '2' },
        {'title': '3', 'payload': '3' },
        {'title': '4', 'payload': '4' },
        {'title': '5', 'payload': '5' }
    ]
}


node_1 = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Vốn\n'
            '2. Chủ sở hữu công ty\n'
            '3. Khác',
    'quick_reply': [
        {'title': '1', 'payload': '1_1' },
        {'title': '2', 'payload': '1_2' },
        {'title': '3', 'payload': '1_3' }
    ]
}

node_3 = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Hội đồng thành viên\n'
            '2. Kiểm soát viên\n'
            '3. Khác',
    'quick_reply': [
        {'title': '1', 'payload': '3_1' },
        {'title': '2', 'payload': '3_2' },
        {'title': '3', 'payload': '3_3' }
    ]
}

node_1_1 = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Thực hiện góp vốn thành lập công ty\n' # dieu 75
            '2. Thay đổi vốn điều lệ\n' # dieu 87
            '3. Khác',
    'quick_reply': [
        {'title': '1', 'payload': '1_1_1' },
        {'title': '2', 'payload': '1_1_2' },
        {'title': '3', 'payload': '1_1_3' }
    ]
}

node_1_2 = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Quyền của chủ sở hữu công ty\n' # dieu 75
            '2. Nghĩa vụ của chủ sở hữu công ty\n' # dieu 76
            '3. Thực hiện quyền của chủ sở hữu công ty trong một số trường hợp đặc biệt\n' # dieu 77
            '4. Khác',
    'quick_reply': [
        {'title': '1', 'payload': '1_2_1' },
        {'title': '2', 'payload': '1_2_2' },
        {'title': '3', 'payload': '1_2_3' },
        {'title': '4', 'payload': '1_2_4' }
    ]
}

node_3_1 = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Quyền và nghĩa vụ của Hội đồng thành viên\n' # dieu 91
            '2. Tiêu chuẩn và điều kiện đối với thành viên Hội đồng thành viên\n' # dieu 92
            '3. Quyền và nghĩa vụ của các thành viên khác của Hội đồng thành viên\n' # dieu 95
            '4. Khác',
    'quick_reply': [
        {'title': '1', 'payload': '3_1_1' },
        {'title': '2', 'payload': '3_1_2' },
        {'title': '3', 'payload': '3_1_3' },
        {'title': '4', 'payload': '3_1_4' },
    ]
}

node_3_2 = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Tiêu chuẩn và điều kiện đối với Kiểm soát viên\n' # dieu 103
            '2. Trách nhiệm của Kiểm soát viên\n' # dieu 106
            '3. Miễn nhiệm, cách chức Kiểm soát viên\n' # dieu 107
            '4. Khác',
    'quick_reply': [
        {'title': '1', 'payload': '3_2_1' },
        {'title': '2', 'payload': '3_2_2' },
        {'title': '3', 'payload': '3_2_3' },
        {'title': '4', 'payload': '3_2_4' },
    ]
}
