# -*- coding: utf-8 -*-
__author__ = 'Taikor'

import requests
import json


class TencentNLP():
    def __init__(self):
        self.api_key = r"b7bd03fa8657303ec198"
        self.api_token = r""
        self.user_id = 2481998442
        self.api_token_url = r"http://api.nlp.qq.com/get_token.cgi"
        self.pos_segmentation_url = r"http://api.nlp.qq.com/lexical/analysis"
        self.sentiment_url = r"http://api.nlp.qq.com/text/sentiment"
        self.pos_url = r"http://api.nlp.qq.com/lexical/analysis"

        get_api_token_params = {"user": self.user_id, "key": self.api_key}
        get_api_token_r = requests.get(self.api_token_url, params=get_api_token_params)
        get_api_token_response_body = json.loads(get_api_token_r.text)
        self.api_token = get_api_token_response_body["token"]
        print(self.api_token)

        self.request_header = {
               "Content-Type": "application/json",
               "Accept": "application/json",
               "S-Token": self.api_token
        }

    def sentiment(self, my_text):
        post_data = {"content": my_text}
        r = requests.post(self.sentiment_url, data=post_data, headers=self.request_header)
        #r = requests.post("http://www.baidu.com", data=post_data, headers=request_header)
        print(r.text)

    def pos(self, my_text):
        post_data = {"text": my_text, "code": int(0x00200000)}
        r = requests.post(self.pos_url, data=post_data, headers=self.request_header)
        #r = requests.post("http://www.baidu.com", data=post_data, headers=request_header)
        print(r.text)

nlp = TencentNLP()
nlp.pos("今天真爽")

