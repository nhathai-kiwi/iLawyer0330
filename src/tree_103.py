# coding: utf-8

Node = {
    # Node i ung voi item thu 200 + i
    '201': {
        'text': {
            '01': 'Bạn muốn hỏi gì?\n'
                  '1. Quy định chung\n'
                  '2. Hoạt động nộp thuế\n'
                  '3. Thuế tài sản cho đất\n'
                  '4. Thuế tài sản cho nhà ở\n'
                  '5. Thuế tài sản cho tàu bay, du thuyền, ô tô\n'
                  '6. Khác',
            '02': 'あなたは何を求めていますか\n'
                  '1. 一般規定\n'
                  '2. 納税活動\n'
                  '3. 土地の固定資産税\n'
                  '4. 住宅の固定資産税\n'
                  '5. 航空機、ヨット、車の固定資産税\n'
                  '6. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '202'},
            {'title': '2', 'payload': '203'},
            {'title': '3', 'payload': '204'},
            {'title': '4', 'payload': '205'},
            {'title': '5', 'payload': '206'},
            {'title': '6', 'payload': '1000'},
        ],
    },

    '202': {
        'text': {
            '01': 'Quy định chung?\n'
                  '1. Đối tượng chịu thuế\n'
                  '2. Đối tượng không chịu thuế\n'
                  '3. Người nộp thuế\n'
                  '4. Giá tính thuế\n'
                  '5. Thuế suất\n'
                  '6. Khác',
            '02': '一般規定?\n'
                  '1. 課税対象\n'
                  '2. 非課税対象\n'
                  '3. 納税者\n'
                  '4. 課税価格\n'
                  '5. 税率\n'
                  '6. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10002'},
            {'title': '2', 'payload': '10003'},
            {'title': '3', 'payload': '10004'},
            {'title': '4', 'payload': '10007'},
            {'title': '5', 'payload': '10008'},
            {'title': '6', 'payload': '1000'},
        ],
    },

    '203': {
        'text': {
            '01': 'Hoạt động nộp thuế?\n'
                  '1. Các trường hợp miễn thuế\n'
                  '2. Các trường hợp giảm thuế\n'
                  '3. Đăng ký và tính thuế\n'
                  '4. Nộp thuế\n'
                  '5. Chậm nộp thuế\n'
                  '6. Khác',
            '02': '納税活動?\n'
                  '1. 免税の場合\n'
                  '2. 減税の場合\n'
                  '3. 登録と税計算\n'
                  '4. 税金を支払う\n'
                  '5. 税金の滞納\n'
                  '6. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10010'},
            {'title': '2', 'payload': '10011'},
            {'title': '3', 'payload': '10012'},
            {'title': '4', 'payload': '10012'},
            {'title': '5', 'payload': '10013'},
            {'title': '6', 'payload': '1000'},
        ],
    },

    '204': {
        'text': {
            '01': 'Thuế tài sản cho đất?\n'
                  '1. Giá tính thuế\n'
                  '2. Thuế suất\n'
                  '3. Khác',
            '02': '土地の固定資産税?\n'
                  '1. 課税価格\n'
                  '2. 税率\n'
                  '3. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10007'},
            {'title': '2', 'payload': '10008'},
            {'title': '3', 'payload': '1000'},
        ],
    },

    '205': {
        'text': {
            '01': 'Thuế tài sản cho nhà ở?\n'
                  '1. Giá tính thuế\n'
                  '2. Thuế suất\n'
                  '3. Khác',
            '02': '住宅の固定資産税?\n'
                  '1. 課税価格\n'
                  '2. 税率\n'
                  '3. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10007'},
            {'title': '2', 'payload': '10008'},
            {'title': '3', 'payload': '1000'},
        ],
    },

    '206': {
        'text': {
            '01': 'Thuế tài sản cho tàu bay, thuyền, ô tô?\n'
                  '1. Giá tính thuế\n'
                  '2. Thuế suất\n'
                  '3. Khác',
            '02': '航空機、ボート、自動車の固定資産税?\n'
                  '1. 課税価格\n'
                  '2. 税率\n'
                  '3. その他',
        },
        'quick_reply': [
            {'title': '1', 'payload': '10007'},
            {'title': '2', 'payload': '10008'},
            {'title': '3', 'payload': '1000'},
        ],
    },

}