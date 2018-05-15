#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""iLawyer server"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


CONFIG = {
    'FACEBOOK_TOKEN': 'EAAGHCApnutgBAPSI0DYFXxRu1nn7GEOfz9f3mstNpCpo2HNBxpyFYkCrz3QrCYjZAggpLXtkouVfmRcTUAAp6LaQJ5RVgxFcqV93WmSRDuqlrGGccnNJ5oqu4368aiSCdHiuSjYzMDVaph5Af00UaPoOyWZBv53y3xTMWIsmy3S4xleXUZB',
    'VERIFY_TOKEN': 'kiwi_token',
    'SERVER_URL': '',
    'Tokenkey': 'kiwi_token'
}

from flask import Flask, request, send_from_directory
from fbmq import Page
app = Flask(__name__)
import messenger


page = Page(CONFIG['FACEBOOK_TOKEN'])
@page.after_send
def after_send(payload, response):
    print('AFTER_SEND : ' + payload.to_json())
    print('RESPONSE : ' + response.text)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == CONFIG['VERIFY_TOKEN']:#os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    # print "Payload: ", payload
    # hande message at (@page.handle_message def received_message(event) ) in file messenger.py
    page.handle_webhook(payload)
    # tokenkey = request.args.get("hub.tokenkey")
    # print "Tokenkey: ", request.args.iteritems()
    # tokenkey = request.headers['Tokenkey']
    # print "Rqeuest headers: ", tokenkey
    return "OK", 200


@app.route('/api', methods=['POST'])
def webhook_api():
    payload = request.get_data(as_text=True)
    print "Payload: ", payload.encode("utf-8")
    # hande message at (@page.handle_message def received_message(event) ) in file messenger.py
    # page.handle_webhook(payload)

    # tokenkey = request.headers['Tokenkey']
    # value = pr.process_post_request(payload)
    # print "tokenkey: ", tokenkey
    # return value, 200

    if 'Tokenkey' in request.headers:
        tokenkey = request.headers['Tokenkey']
        if tokenkey == CONFIG['Tokenkey']:
            # print tokenkey
            value = pr.process_post_request(payload)
            print "tokenkey: ", tokenkey
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