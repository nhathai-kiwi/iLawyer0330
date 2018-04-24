# coding: utf-8

Node = {

    # Node i ung voi item thu 200 + i
    '201': {
        'text': {
            '01': 'Bạn muốn hỏi gì?\n'
                  '1. Các loại hình công ty\n'
                  '2. Các khái niệm cơ bản\n'
                  '3. Quyền của doanh nghiệp\n'
                  '4. Nghĩa vụ của doanh nghiệp\n'
                  '5. Người đại diện theo pháp luật\n'
                  '6. Thành lập doanh nghiệp\n'
                  '7. Tổ chức lại, giải thể và phá sản',
            '02': 'あなたは何を求めていますか\n'
                  '1. 企業の種類\n'
                  '2. 基本コンセプト\n'
                  '3. 事業の権利\n'
                  '4. 事業の義務\n'
                  '5. 法律上の代表者\n'
                  '6. ビジネスの確立\n'
                  '7. 再編、解散、破産',
        },
        'quick_reply': [
            {'title': '1', 'payload': '202'},
            {'title': '2', 'payload': '10004'},
            {'title': '3', 'payload': '10007'},
            {'title': '4', 'payload': '10008'},
            {'title': '5', 'payload': '10014'},
            {'title': '6', 'payload': '213'},
            {'title': '7', 'payload': '214'},
        ],
    },

    '202': {
        'text': {
            '01': 'Các loại hình công ty?\n'
                  '1. Trách nhiệm hữu hạn 2 thành viên trở \n'
                  '2. Trách nhiệm hữu hạn 1 thành viên\n'
                  '3. Doanh nghiệp nhà nước\n'
                  '4. Công ty cổ phần\n'
                  '5. Công ty hợp danh\n'
                  '6. Doanh nghiệp tư nhân',
            '02': '企業の種類?\n'
                  '1. 2人以上のメンバーの責任限定\n'
                  '2. 1メンバー有限責任\n'
                  '3. 国有企業\n'
                  '4. 合資会社\n'
                  '5. パートナーシップ\n'
                  '6. 民間企業',
        },
        'quick_reply': [
            {'title': '1', 'payload': '203'},
            {'title': '2', 'payload': '207'},
            {'title': '3', 'payload': '208'},
            {'title': '4', 'payload': '209'},
            {'title': '5', 'payload': '211'},
            {'title': '6', 'payload': '212'},
        ],
    },

    '203': {
        'text': {
            '01': 'Trách nhiệm hữu hạn 2 thành viên trở lên?\n'
                  '1. Định nghĩa\n'
                  '2. Vốn\n'
                  '3. Quyền của thành viên\n'
                  '4. Nghĩa vụ của thành viên\n'
                  '5. Hội đồng thành viên\n'
                  '6. Giám đốc, Tổng giám đốc\n'
                  '7. Khác',
            '02': '2人以上のメンバーの責任限定?\n'
                  '1. 定義\n'
                  '2. 首都\n'
                  '3. メンバーシップの権利\n'
                  '4. 会員義務\n'
                  '5. 会員協議会n\n'
                  '6. 取締役、総監督\n'
                  '7. その他'
        },
        'quick_reply': [
            {'title': '1', 'payload': '10047'},
            {'title': '2', 'payload': '204'},
            {'title': '3', 'payload': '10050'},
            {'title': '4', 'payload': '10051'},
            {'title': '5', 'payload': '205'},
            {'title': '6', 'payload': '206'},
            {'title': '7', 'payload': '1000'},
        ],
    },

    '204': {
        'text': {
            '01': 'Vốn?\n'
                  '1. Định nghĩa\n'
                  '2. Mua lại vốn góp\n'
                  '3. Chuyển nhượng vốn góp\n'
                  '4. Thay đổi\n'
                  '5. Khác',
            '02': '首都?\n'
                  '1. 定義\n'
                  '2. 資本拠出の買戻し\n'
                  '3. 寄付資本の移転\n'
                  '4. 変更\n'
                  '5. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10048'},
            {'title': '2', 'payload': '10052'},
            {'title': '3', 'payload': '10053'},
            {'title': '4', 'payload': '10068'},
            {'title': '5', 'payload': '1000'},
        ],
    },

    '205': {
        'text': {
            '01': 'Hội đồng thành viên?\n'
                  '1. Định nghĩa\n'
                  '2. Chủ tịch\n'
                  '3. Triệu tập họp\n'
                  '4. Nghị quyết\n'
                  '5. Biên bản\n'
                  '6. Khác',
            '02': '会員協議会?\n'
                  '1. 定義\n'
                  '2. 大統領\n'
                  '3. 会議に出席する\n'
                  '4. 解像度\n'
                  '5. 分\n'
                  '6. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10056'},
            {'title': '2', 'payload': '10057'},
            {'title': '3', 'payload': '10058'},
            {'title': '4', 'payload': '10060'},
            {'title': '5', 'payload': '10061'},
            {'title': '6', 'payload': '1000'},
        ],
    },

    '206': {
        'text': {
            '01': 'Giám đốc, Tổng giám đốc?\n'
                  '1. Định nghĩa\n'
                  '2. Tiêu chuẩn, điều kiện',
            '02': '取締役、総監督?\n'
                  '1. 定義\n'
                  '2. 基準、条件',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10064'},
            {'title': '2', 'payload': '10065'},
        ],
    },

    '207': {
        'text': {
            '01': 'Trách nhiệm hữu hạn 1 thành viên?\n'
                  '1. Định nghĩa\n'
                  '2. Vốn\n'
                  '3. Quyền của chủ sở hữu\n'
                  '4. Nghĩa vụ của chủ sở hữu\n'
                  '5. Hội đồng thành viên\n'
                  '6. Chủ tịch công ty\n'
                  '7. Giám đốc, Tống giám đốc\n'
                  '8. Khác',
            '02': '1メンバー有限責任?\n'
                  '1. 定義\n'
                  '2. 首都\n'
                  '3. オーナーの権利\n'
                  '4. 所有者の義務\n'
                  '5. 会員協議会\n'
                  '6. 会社の社長\n'
                  '7. トンディレクターディレクター\n'
                  '8. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10073'},
            {'title': '2', 'payload': '10074'},
            {'title': '3', 'payload': '10075'},
            {'title': '4', 'payload': '10076'},
            {'title': '5', 'payload': '10079'},
            {'title': '6', 'payload': '10080'},
            {'title': '7', 'payload': '10081'},
            {'title': '8', 'payload': '1000'},
        ],
    },

    '208': {
        'text': {
            '01': 'Doanh nghiệp nhà nước?\n'
                  '1. Hội đồng thành viên\n'
                  '2. Chủ tịch công ty\n'
                  '3. Giám đốc, Tống giám đốc\n'
                  '4. Ban kiểm soát và kiểm soát viên',
            '02': '国有企業?\n'
                  '1. 会員協議会\n'
                  '2. 会社の社長\n'
                  '3. トンディレクターディレクター\n'
                  '4. コントロールボードとコントローラ',
        },
        'quick_reply': [
            {'title': '1', 'payload': '1000'},
            {'title': '2', 'payload': '10098'},
            {'title': '3', 'payload': '1000'},
            {'title': '4', 'payload': '1000'},
        ],
    },

    '209': {
        'text': {
            '01': 'Công ty cổ phần?\n'
                  '1. Định nghĩa\n'
                  '2. Vốn\n'
                  '3. Quyền của cổ đông phổ thông\n'
                  '4. Cố phiếu\n'
                  '5. Chuyển nhượng cổ phần\n'
                  '6. Đại hội đồng cổ đông\n'
                  '7. Hội đồng quản trị\n'
                  '8. Khác',
            '02': '合資会社?\n'
                  '1. 定義\n'
                  '2. 首都\n'
                  '3. 普通株主の権利\n'
                  '4. 株式\n'
                  '5. 株式移転\n'
                  '6. 株主総会\n'
                  '7. 取締役会\n'
                  '8. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10110'},
            {'title': '2', 'payload': '10111'},
            {'title': '3', 'payload': '10114'},
            {'title': '4', 'payload': '10120'},
            {'title': '5', 'payload': '10126'},
            {'title': '6', 'payload': '10135'},
            {'title': '7', 'payload': '210'},
            {'title': '8', 'payload': '1000'},
        ],
    },

    '210': {
        'text': {
            '01': 'Hội đồng quản trị?\n'
                  '1. Định nghĩa\n'
                  '2. Nhiệm kỳ và số lượng\n'
                  '3. Chủ tịch\n'
                  '4. Cuộc họp hội đồng quản trị\n'
                  '5. Giám đốc, Tống giám đốc\n'
                  '6. Ban kiểm soát\n'
                  '7. Khác',
            '02': '取締役会?\n'
                  '1. 定義\n'
                  '2. テニュアと番号\n'
                  '3. 大統領\n'
                  '4. 取締役会\n'
                  '5. トンディレクターディレクター\n'
                  '6. コントロールボード\n'
                  '7. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10149'},
            {'title': '2', 'payload': '10150'},
            {'title': '3', 'payload': '10152'},
            {'title': '4', 'payload': '10153'},
            {'title': '5', 'payload': '10157'},
            {'title': '6', 'payload': '10163'},
            {'title': '7', 'payload': '1000'},
        ],
    },

    '211': {
        'text': {
            '01': 'Công ty hợp danh?\n'
                  '1. Định nghĩa\n'
                  '2. Vốn\n'
                  '3. Quyền của thành viên hợp danh\n'
                  '4. Nghĩa vụ của thành viên hợp danh\n'
                  '5. Hội đồng thành viên\n'
                  '6. Khác',
            '02': 'パートナーシップ?\n'
                  '1. 定義\n'
                  '2. 首都\n'
                  '3. パートナーシップメンバーの権利\n'
                  '4. パートナーシップ会員の義務\n'
                  '5. 会員協議会\n'
                  '6. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10172'},
            {'title': '2', 'payload': '10173'},
            {'title': '3', 'payload': '10176'},
            {'title': '4', 'payload': '10176'},
            {'title': '5', 'payload': '10177'},
            {'title': '6', 'payload': '1000'},
        ],
    },

    '212': {
        'text': {
            '01': 'Doanh nghiệp tư nhân?\n'
                  '1. Khác',
            '02': '民間企業?\n'
                  '1. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '1000'},
        ],
    },

    '213': {
        'text': {
            '01': 'Thành lập doanh nghiệp?\n'
                  '1. Khác',
            # TODO chuyen sang tieng Nhat
            '02': 'ビジネスの確立?\n'
                  '1. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '1000'},
        ],
    },

    '214': {
        'text': {
            '01': 'Tổ chức lại, giải thể và phá sản?\n'
                  '1. Khác',
            # TODO chuyen sang tieng Nhat
            '02': '再編、解散、破産?\n'
                  '1. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '1000'},
        ],
    },
}