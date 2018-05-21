#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""iLawyer server"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from flask import Flask, request, send_from_directory
from fbpage import page
import fbpage
app = Flask(__name__)
import messenger
import iLawyer_firebase as ifb

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == fbpage.CONFIG['VERIFY_TOKEN']:#os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    # print "Payload: ", payload
    # hande message at (@page.handle_message def received_message(event) ) in file messenger.py
    page.handle_webhook(payload)
    return "OK", 200


@app.route('/gfb', methods=['POST'])
def gg_firebase():
    payload = request.get_data(as_text=True)
    print "Payload: ", payload.encode('utf-8')

    if 'Tokenkey' in request.headers:
        tokenkey = request.headers['Tokenkey']
        if tokenkey == fbpage.CONFIG['Tokenkey']:
            print tokenkey
            value = ifb.handle_post_request(payload)
            # value = "TJASFDJFS"
            print "tokenkey: ", tokenkey
            print "value: ", value
            return value, 200

        else:
            return "Request denied!", 200
    else:
        return "Request denied!", 100


@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)

if __name__ == '__main__':
    app.run(port=5000, debug=True, threaded=True)

# chcp 65001