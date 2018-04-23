Node = {

    # Node i ung voi item thu 200 + i
    '201': {
        'text': {
            '01': 'Bạn muốn hỏi gì?\n'
                  '1. Tìm hiểu về các khái niệm cơ bản\n'
                  '2. Phân loại đất\n'
                  '3. Giấy chứng nhận quyền sử dụng đất\n'
                  '4. Tranh chấp đất đai\n'
                  '5. Thu hồi\n'
                  '6. Bồi thường\n'
                  '7. Chuyển nhượng',
            '02': 'あなたは何を求めていますか？'
                  '1. 基本的な概念について学ぶ\n'
                  '2. 土地の分類\n'
                  '3. 土地使用権証明書\n'
                  '4. 土地紛争\n'
                  '5. 失効\n'
                  '6. 報酬\n'
                  '7. 割り当て',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10003'},
            {'title': '2', 'payload': '10010'},
            {'title': '3', 'payload': '202'},
            {'title': '4', 'payload': '203'},
            {'title': '5', 'payload': '204'},
            {'title': '6', 'payload': '206'},
            {'title': '7', 'payload': '1000'},
        ],
    },

    '202': {
        'text': {
            '01': 'Giấy chứng nhận quyền sử dụng đất?\n'
                  '1. Đang sử dụng và có giấy tờ\n'
                  '2. Đang sử dụng và không có giấy tờ\n'
                  '3. Cấp cho tổ chức, cơ sở tôn giáo đang sử dụng\n'
                  '4. Cấp cho tài sản gắn liền với đất\n'
                  '5. Thẩm quyền cấp\n',
            '02': '土地使用権証明書?\n'
                  '1. 使用され、論文を持っている\n'
                  '2. 使用され、文書化されていない\n'
                  '3. 使用中の組織や宗教施設に発行される\n'
                  '4. 土地に附属する資産の譲渡\n'
                  '5. 権限が発行されました\n',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10100'},
            {'title': '2', 'payload': '10101'},
            {'title': '3', 'payload': '10102'},
            {'title': '4', 'payload': '10104'},
            {'title': '5', 'payload': '10105'},
        ],
    },

    '203': {
        'text': {
            '01': 'Tranh chấp đất đai?\n'
                  '1. Hòa giải\n'
                  '2. Thẩm quyền giải quyết tranh chấp',
            '02': '土地紛争?\n'
                  '1. 調停\n'
                  '2. 紛争解決能力',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10202'},
            {'title': '2', 'payload': '10203'},
        ],
    },

    '204': {
        'text': {
            '01': 'Thu hồi?\n'
                  '1. Các trường hợp thu hồi\n'
                  '2. Thẩm quyền thu hồi',
            '02': '失効?\n'
                  '1. リコールのケース\n'
                  '2. 失効の管轄',
        },
        'quick_reply': [
            {'title': '1', 'payload': '205'},
            {'title': '2', 'payload': '10066'},
        ],
    },

    '205': {
        'text': {
            '01': 'Các trường hợp thu hồi?\n'
                  '1. Quốc phòng, an ninh\n'
                  '2. Lợi ích công cộng\n'
                  '3. Vi phạm pháp luật về đất đai\n'
                  '4. Khác\n',
            '02': 'リコールのケース?\n'
                  '1. 防衛と安全\n'
                  '2. 公益\n'
                  '3. 土地法を破る\n'
                  '4. その他\n',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10061'},
            {'title': '2', 'payload': '10062'},
            {'title': '3', 'payload': '10064'},
            {'title': '4', 'payload': '1000'},
        ],
    },

    '206': {
        'text': {
            '01': 'Bồi thường?\n'
                  '1. Bồi thường về đất\n'
                  '2. Bồi thường về tài sản',
            '02': '取締役、総監督?\n'
                  '1. 定義\n'
                  '2. 基準、条件',
        },
        'quick_reply': [
            {'title': '1', 'payload': '207'},
            {'title': '2', 'payload': '210'},
        ],
    },

    '207': {
        'text': {
            '01': 'Bồi thường về đất?\n'
                  '1. Nguyên tắc bồi thường về đất\n'
                  '2. Điều kiện được bồi thường về đất\n'
                  '3. Các trường hợp bồi thường về đất\n'
                  '4. Hỗ trợ ngoài bồi thường về đất',
            '01': '土地補償?\n'
                  '1. 土地補償の原則\n'
                  '2. 土地補償の条件\n'
                  '3. 土地補償の場合\n'
                  '4. 土地補償のサポート',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10074'},
            {'title': '2', 'payload': '10075'},
            {'title': '3', 'payload': '208'},
            {'title': '4', 'payload': '209'},
        ],
    },


    '208': {
        'text': {
            '01': 'Các trường hợp bồi thường về đất?\n'
                  '1. Quốc phòng, an ninh, lợi ích công cộng\n'
                  '2. Đất nông nghiệp\n'
                  '3. Tổ chức kinh tế, công đồng dân cư, cơ sở tôn giáo\n'
                  '4. Đất ở\n'
                  '5. Đất phi nông nghiệp không phải đất ở của cá nhân, hộ gia đình\n'
                  '6. Đất phi nông nghiệp không phải đất ở của tổ chức kinh tế, cộng đồng dân cư, cơ sở tôn giáo, ng vn ở nc ngoài, tổ chức nc ngoài\n'
                  '7. Trường hợp không đc bồi thường',
            '02': '土地補償の場合?\n'
                  '1. 防衛、安全保障、公益\n'
                  '2. 農地\n'
                  '3. 経済団体、地域社会、宗教施設\n'
                  '4. 住宅地\n'
                  '5. 非農地は個人または世帯の居住地ではない\n'
                  '6. 非農地は経済団体、居住コミュニティ、宗教施設、外国人、外国団体の居住地ではない\n'
                  '7. ケースは補償されません',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10076'},
            {'title': '2', 'payload': '10077'},
            {'title': '3', 'payload': '10078'},
            {'title': '4', 'payload': '10079'},
            {'title': '5', 'payload': '10080'},
            {'title': '6', 'payload': '10081'},
            {'title': '7', 'payload': '10082'},
        ],
    },


    '209': {
        'text': {
            '01': 'Hỗ trợ ngoài bồi thường về đất?\n'
                  '1. Nguyên tắc hỗ trợ\n'
                  '2. Các khoản hỗ trợ\n'
                  '3. Hộ trợ đào tạo, chuyển đổi nghề, tìm kiếm việc làm\n'
                  '4. Tái định cư\n'
                  '5. Tái định cư\n'
                  '6. Tái định cư\n',
            '02': '土地補償のサポート?\n'
                  '1. サポートの原則\n'
                  '2. 資金\n'
                  '3. トレーニングサポート、求人情報の変更、求人検索\n'
                  '4. 移転\n'
                  '5. 移転\n'
                  '6. 移転\n',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10183'},
            {'title': '2', 'payload': '10183'},
            {'title': '3', 'payload': '10184'},
            {'title': '4', 'payload': '10185'},
            {'title': '5', 'payload': '10186'},
            {'title': '6', 'payload': '10187'},
        ],
    },

    '210': {
        'text': {
            '01': 'Bồi thường về tài sản?\n'
                  '1. Nguyên tắc bồi thường về tài sản\n'
                  '2. Các trường hợp bồi thường về tài sản\n'
                  '3. Hỗ trợ ngoài bồi thường về tài sản',
            '02': '財産に対する補償?\n'
                  '1. 財産の補償の原則\n'
                  '2. 財産に対する補償\n'
                  '3. 財産補償に加えて支援',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10088'},
            {'title': '2', 'payload': '211'},
            {'title': '3', 'payload': '212'},
        ],
    },

    '211': {
        'text': {
            '01': 'Các trường hợp bồi thường về tài sản?\n'
                  '1. Thiệt hại về nhà, công trình\n'
                  '2. Cây trồng, vật nuôi\n'
                  '3. Chi phí di chuyển\n'
                  '4. Trường hợp không được bồi thường\n'
                  '5. Chi trả tiền bồi thường, hỗ trợ, tái định cư\n'
                  '6. Hành lang an toàn',
            '02': '財産に対する補償?\n'
                  '1. 家へのダメージ、作品\n'
                  '2. 作物と家畜\n'
                  '3. 旅費\n'
                  '4. ケースは補償されません\n'
                  '5. 補償、支援、再定住のための支払い\n'
                  '6. 安全通路',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10089'},
            {'title': '2', 'payload': '10090'},
            {'title': '3', 'payload': '10091'},
            {'title': '4', 'payload': '10092'},
            {'title': '5', 'payload': '10093'},
            {'title': '6', 'payload': '10094'},
        ],
    },


    '212': {
        'text': {
            '01': 'Hỗ trợ ngoài bồi thường về tài sản?\n'
                  '1. Khác',
            '02': '財産補償に加えて支援?\n'
                  '1. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '1000'},
        ],
    },

}
