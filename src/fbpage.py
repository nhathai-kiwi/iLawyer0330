#!/usr/bin/env python
# -*- coding: utf-8 -*-


CONFIG = {
    'FACEBOOK_TOKEN': 'EAAGHCApnutgBAPSI0DYFXxRu1nn7GEOfz9f3mstNpCpo2HNBxpyFYkCrz3QrCYjZAggpLXtkouVfmRcTUAAp6LaQJ5RVgxFcqV93WmSRDuqlrGGccnNJ5oqu4368aiSCdHiuSjYzMDVaph5Af00UaPoOyWZBv53y3xTMWIsmy3S4xleXUZB',
    'VERIFY_TOKEN': 'kiwi_token',
    'SERVER_URL': '',
    'Tokenkey': 'kiwi_token'
}

from fbmq import Page

page = Page(CONFIG['FACEBOOK_TOKEN'])


@page.after_send
def after_send(payload, response):
    print('AFTER_SEND : ' + payload.to_json())
    print('RESPONSE : ' + response.text)
