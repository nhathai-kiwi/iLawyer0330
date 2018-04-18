# coding: utf-8
import os
import sys
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path = os.path.dirname(os.path.abspath(__file__))
path_run_NLP = path.replace('/chat-bot-Messenger', '/src')
sys.path.insert(0, path_run_NLP)
print path_run_NLP
import main

# os.sys.path.insert(0,parentdir)
# print parentdir
import openpyxl
from config import CONFIG
import config
from fbmq import Attachment, Template, QuickReply, NotificationType
from facebook_page import page

