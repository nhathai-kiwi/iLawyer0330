# coding: utf-8
from fbmq import QuickReply
from fbmq import Attachment, Template, QuickReply, Page

CONFIG = {
    'FACEBOOK_TOKEN': 'EAAGHCApnutgBAPSI0DYFXxRu1nn7GEOfz9f3mstNpCpo2HNBxpyFYkCrz3QrCYjZAggpLXtkouVfmRcTUAAp6LaQJ5RVgxFcqV93WmSRDuqlrGGccnNJ5oqu4368aiSCdHiuSjYzMDVaph5Af00UaPoOyWZBv53y3xTMWIsmy3S4xleXUZB',
    'VERIFY_TOKEN': 'kiwi_token',
    'SERVER_URL': '',
    'Tokenkey': 'kiwi_token'
}

final_answer = 'Đề nghị tư vấn luật sư để có câu trả lời chính xác'
final_answer_ja = '正しい答えは弁護士に相談してください'

prefer_question_vi = 'Xin mời bạn đưa ra nội dung câu hỏi'
prefer_question_ja = '質問を入力してください'

law_in_enterprise_xlsx = 'lawInEnterprise.xlsx'

node_root = {
    'text': 'Bạn muốn hỏi về?\n'
            '1. Công ty trách nhiệm hữu hạn một thành viên\n'
            '2. Công ty trách nhiệm hữu hạn hai thành viên trở lên\n'
            '3. Doanh nghiệp nhà nước\n'
            '4. Công ty cổ phần\n'
            '5. Kết nối luật sư',

    'quick_reply': [
        {'title': '1', 'payload': '1' },
        {'title': '2', 'payload': '2' },
        {'title': '3', 'payload': '3' },
        {'title': '4', 'payload': '4' },
        {'title': '5', 'payload': '5' }
    ],

    'key_words': [
        {'title': '1', 'word': ['trách nhiệm hữu hạn một thành viên'] },
        {'title': '2', 'word': ['trách nhiệm hữu hạn hai thành viên trở lên']},
        {'title': '3', 'word': ['Doanh nghiệp nhà nước'] },
        {'title': '4', 'word': ['cổ phần'] },
        {'title': '5', 'word': [] }
    ],
    'text_ja': '何を聞きたいですか\n'
            '1. ワンメンバー有限責任会社\n'
            '2. 2人以上のメンバーを持つ有限責任会社\n'
            '3. 国有企業\n'
            '4. 合資会社\n'
            '5. 弁護士をつなぐ'
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
    ],

    'key_words': [
        {'title': '1', 'word': ['Vốn']},
        {'title': '2', 'word': ['Chủ sở hữu công ty']},
        {'title': '3', 'word': []}
    ],
    'text_ja': '何を聞きたいですか\n'
               '1. 首都\n'
               '2. 会社のオーナー\n'
               '3. その他\n'
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
    ],

    'key_words': [
        {'title': '1', 'word': ['Hội đồng thành viên']},
        {'title': '2', 'word': ['Kiểm soát viên']},
        {'title': '3', 'word': []}
    ],
    'text_ja': '何を聞きたいですか\n'
               '1. 会員協議会\n'
               '2. 監督者\n'
               '3. その他\n'
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
    ],
    'text_ja': '何を聞きたいですか\n'
               '1. 会社を設立するために資本貢献する\n'
               '2. チャーター・キャピタルの変更\n'
               '3. その他\n'
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
    ],
    'text_ja': '何を聞きたいですか\n'
               '1. 会社の所有者の権利\n'
               '2. 会社の所有者の義務\n'
               '3. 特定の特殊なケースでは、会社の所有者の権利を行使する\n'
               '4. その他'
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
    ],
    'text_ja': '何を聞きたいですか\n'
               '1. 理事会の権利と義務\n'
               '2. 会員評議会メンバーの基準と条件\n'
               '3. 会員評議会の他のメンバーの権利と義務\n'
               '4. その他'
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
    ],
    'text_ja': '何を聞きたいですか\n'
               '1. 検査官の基準と条件\n'
               '2. 監督者の責任\n'
               '3. 解雇、解雇監督\n'
               '4. その他'
}

node_add_question = {
    'text': 'Bạn có muốn tiếp tục đặt câu hỏi nữa không?\n',
    'quick_reply': [
        {'title': 'Có', 'payload': 'yes' },
        {'title': 'Không', 'payload': 'no' },
    ],
    'quick_reply_ja': [
        {'title': 'はい', 'payload': 'yes' },
        {'title': 'いいえ。', 'payload': 'no' },
    ],
    'text_ja' : 'あなたは質問を続けておきたいですか'

}

node_choose_language = {
    'text': 'Which language would you like to use?\n',
    'quick_reply': [
        {'title': 'vietnamese', 'payload': 'vi' },
        {'title': 'japanese', 'payload': 'ja' },
    ]

}

node_test_text = {
    'text':{
        'vi': 'Which language would you like to use?\n',
        'ja': 'あなたは質問を続けておきたいですか'
    },
    'quick_reply': [
        {'title': 'vietnamese', 'payload': 'vi' },
        {'title': 'japanese', 'payload': 'ja' },
    ]

}

