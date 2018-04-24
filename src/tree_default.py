# coding: utf-8

Tree =  {
    # lua chon ngon ngu, payload danh so tu 01 --> 99
    '0': {
        'text': 'Which language would you like to use',
        'quick_reply': [
            {'title': 'vietnamese', 'payload': '01'},
            {'title': '日本語', 'payload': '02'},
        ]
    },

    # lua chon cac button quick_reply, payload danh so tu 100 -> 999
    # cac loai luat danh so tu 101 den 199
    # danh dau cac bo luat: Luat doanh nghiep 101, luat dat dai 102

    '100': {
        'text': {
            # 'What area of law are you interested in?',
            '01': 'Lĩnh vực luật bạn quan tâm?\n'
                  '1. Luật doanh nghiệp\n'
                  '2. Luật đất đai',

            '02': '興味のある法律分野ですか?\n'
                  '1. 企業法は、\n'
                  '2. 土地法',
        },
        'quick_reply': [
            {'title': '1', 'payload': '101'},
            {'title': '2', 'payload': '102'},
        ]
    },
    # xu li cac node noi bo trong tree (ko phai nut la, cac nut co quick reply dua ra goi y cho nguoi dung) trong mot bo luat
    # phan xu li cac node nay co trong cac file tree_101.py, tree_102.py,...
    # payload danh so tu 200 den 999



    # lua chon cac nut la tuong ung voi dieu luat da co san, payload danh so tu 1000 --> 1999
    # payload = 1000, dua ra cau hoi cho nguoi dung
    '1000': {
        'text': {
            '01': 'Xin mời bạn đưa ra nội dung câu hỏi:',
            '02': '質問を入力してください:'
        }
    },



    # xu li cac text, payload tu 2000 -> 2999
    # payload = 100 quay lai tree, dua ra cac lua chon hoi ve loai luat cho nguoi dung
    # payload = 2001, ket thuc tin nhan cua nguoi dung
    '2000': {
        'text':{
            '01': 'Bạn có muốn tiếp tục đặt câu hỏi nữa không?',
            '02': 'あなたは質問を続けておきたいですか'
        },
        'quick_reply': {
            '01':[
                {'title': 'Có', 'payload': '100'},
                {'title': 'Không', 'payload': '2001'}
            ],
            '02':[
                {'title': 'はい', 'payload': '100'},
                {'title': 'いいえ。', 'payload': '2001'}
            ]
        }
    },

    # tin nhan danh dau nguoi dung ket thuc cau hoi
    '2001': {
        'text': {
            '01': 'Trên đây là nội dung tư vấn của iLawyer. Nếu còn vướng mắc chưa rõ cần luật sư giải đáp, bạn vui lòng gọi đến 09xxx...',
            '02': '上記はiLawyerのアドバイスです。 それでも問題が解決しない場合は、09xxxまでご連絡ください。'
        }
    },
}