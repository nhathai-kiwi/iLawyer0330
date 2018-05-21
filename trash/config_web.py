# coding: utf-8
from fbmq import QuickReply
from fbmq import Attachment, Template, QuickReply, Page

CONFIG = {
    'FACEBOOK_TOKEN': 'EAAGHCApnutgBAF9XYSeL7ZCy4At0uZAv9GNFKxhNr8ZC4xcRCrnxbLdlVa9d1o9yZC1bDo18Xzx8Omc2qUUKnECDsjx67A3G2mNeO7rX5NzA4LXXYCCVqp32EyBtbcDmjLpq06ZAMtljZBA2jM0iO7zN8WpHj6No9UzBd5H6bzfn2Q97oyrfq6',
    'VERIFY_TOKEN': 'kiwi_token',
    'SERVER_URL': '2738a848.ngrok.io',
    'Tokenkey': 'kiwi_token'
}
law_in_enterprise_xlsx = 'lawInEnterprise.xlsx'

final_answer = {
    'vi': 'Đề nghị tư vấn luật sư để có câu trả lời chính xác',
    'ja': '正しい答えは弁護士に相談してください'
}

prefer_question = {
    'vi': 'Xin mời bạn đưa ra nội dung câu hỏi',
    'ja': '質問を入力してください'
}

prefer_lawyer = {
    'vi': 'Dưới đây là thông tin luật sư ...',
    'ja': '弁護士の情報はここにあります...'
}

last_message = {
    'vi': 'Trên đây là nội dung tư vấn của iLawyer. Nếu còn vướng mắc chưa rõ cần luật sư giải đáp, bạn vui lòng gọi đến ...',
    'ja': '上記はiLawyerのアドバイスです。 問題が明らかでない場合は、弁護士に電話して、電話してください...'
}

node_root = {
    'text': {
        'vi': 'Bạn muốn hỏi về?\n'
            '1. Công ty trách nhiệm hữu hạn một thành viên\n'
            '2. Công ty trách nhiệm hữu hạn hai thành viên trở lên\n'
            '3. Doanh nghiệp nhà nước\n'
            '4. Công ty cổ phần\n'
            '5. Kết nối luật sư',
        'ja': '何を聞きたいですか\n'
            '1. ワンメンバー有限責任会社\n'
            '2. 2人以上のメンバーを持つ有限責任会社\n'
            '3. 国有企業\n'
            '4. 合資会社\n'
            '5. 弁護士をつなぐ'
    },
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
    ]
}


node_1 = {
    'text': {
        'vi': 'Bạn muốn hỏi về?\n'
            '1. Vốn\n'
            '2. Chủ sở hữu công ty\n'
            '3. Khác',
        'ja': '何を聞きたいですか\n'
               '1. 首都\n'
               '2. 会社のオーナー\n'
               '3. その他'
    },

    'quick_reply': [
        {'title': '1', 'payload': '1_1' },
        {'title': '2', 'payload': '1_2' },
        {'title': '3', 'payload': '1_3' }
    ],

    'key_words': [
        {'title': '1', 'word': ['Vốn']},
        {'title': '2', 'word': ['Chủ sở hữu công ty']},
        {'title': '3', 'word': []}
    ]
}

node_3 = {
    'text': {
        'vi': 'Bạn muốn hỏi về?\n'
            '1. Hội đồng thành viên\n'
            '2. Kiểm soát viên\n'
            '3. Khác',
        'ja': '何を聞きたいですか\n'
               '1. 会員協議会\n'
               '2. 監督者\n'
               '3. その他'
    },
    'quick_reply': [
        {'title': '1', 'payload': '3_1' },
        {'title': '2', 'payload': '3_2' },
        {'title': '3', 'payload': '3_3' }
    ],

    'key_words': [
        {'title': '1', 'word': ['Hội đồng thành viên']},
        {'title': '2', 'word': ['Kiểm soát viên']},
        {'title': '3', 'word': []}
    ]
}

node_1_1 = {
    'text': {
        'vi':'Bạn muốn hỏi về?\n'
            '1. Thực hiện góp vốn thành lập công ty\n' # dieu 75
            '2. Thay đổi vốn điều lệ\n' # dieu 87
            '3. Khác',
        'ja': '何を聞きたいですか\n'
               '1. 会社を設立するために資本貢献する\n'
               '2. チャーター・キャピタルの変更\n'
               '3. その他'
    },
    'quick_reply': [
        {'title': '1', 'payload': '1_1_1' },
        {'title': '2', 'payload': '1_1_2' },
        {'title': '3', 'payload': '1_1_3' }
    ]
}

node_1_2 = {
    'text': {
        'vi': 'Bạn muốn hỏi về?\n'
            '1. Quyền của chủ sở hữu công ty\n' # dieu 75
            '2. Nghĩa vụ của chủ sở hữu công ty\n' # dieu 76
            '3. Thực hiện quyền của chủ sở hữu công ty trong một số trường hợp đặc biệt\n' # dieu 77
            '4. Khác',
        'ja': '何を聞きたいですか\n'
               '1. 会社の所有者の権利\n'
               '2. 会社の所有者の義務\n'
               '3. 特定の特殊なケースでは、会社の所有者の権利を行使する\n'
               '4. その他'
    },
    'quick_reply': [
        {'title': '1', 'payload': '1_2_1' },
        {'title': '2', 'payload': '1_2_2' },
        {'title': '3', 'payload': '1_2_3' },
        {'title': '4', 'payload': '1_2_4' }
    ]
}

node_3_1 = {
    'text': {
        'vi': 'Bạn muốn hỏi về?\n'
            '1. Quyền và nghĩa vụ của Hội đồng thành viên\n' # dieu 91
            '2. Tiêu chuẩn và điều kiện đối với thành viên Hội đồng thành viên\n' # dieu 92
            '3. Quyền và nghĩa vụ của các thành viên khác của Hội đồng thành viên\n' # dieu 95
            '4. Khác',
        'ja': '何を聞きたいですか\n'
               '1. 理事会の権利と義務\n'
               '2. 会員評議会メンバーの基準と条件\n'
               '3. 会員評議会の他のメンバーの権利と義務\n'
               '4. その他'
    },
    'quick_reply': [
        {'title': '1', 'payload': '3_1_1' },
        {'title': '2', 'payload': '3_1_2' },
        {'title': '3', 'payload': '3_1_3' },
        {'title': '4', 'payload': '3_1_4' },
    ]
}

node_3_2 = {
    'text':{
        'vi': 'Bạn muốn hỏi về?\n'
            '1. Tiêu chuẩn và điều kiện đối với Kiểm soát viên\n' # dieu 103
            '2. Trách nhiệm của Kiểm soát viên\n' # dieu 106
            '3. Miễn nhiệm, cách chức Kiểm soát viên\n' # dieu 107
            '4. Khác',
        'ja': '何を聞きたいですか\n'
               '1. 検査官の基準と条件\n'
               '2. 監督者の責任\n'
               '3. 解雇、解雇監督\n'
               '4. その他'
    },
    'quick_reply': [
        {'title': '1', 'payload': '3_2_1' },
        {'title': '2', 'payload': '3_2_2' },
        {'title': '3', 'payload': '3_2_3' },
        {'title': '4', 'payload': '3_2_4' },
    ]
}

node_add_question = {
    'text':{
        'vi': 'Bạn có muốn tiếp tục đặt câu hỏi nữa không?',
        'ja': 'あなたは質問を続けておきたいですか'
    },
    'quick_reply': {
        'vi':[
            {'title': 'Có', 'payload': 'yes' },
            {'title': 'Không', 'payload': 'no' }
        ],
        'ja':[
            {'title': 'はい', 'payload': 'yes' },
            {'title': 'いいえ。', 'payload': 'no' }
        ]
    }

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

