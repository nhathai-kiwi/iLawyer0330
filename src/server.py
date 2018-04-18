# coding: utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from flask import Flask, request, send_from_directory, render_template
from fbmq import Event, QuickReply
from config import CONFIG
from facebook_page import page
import messenger
import process_request as pr

import json
app = Flask(__name__)


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