# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('TnssC6Ie7mnWoUmddXHmQqqyRuKl8d349ktLS4m7RYIWO9CVtagYEGXMo9RQ+fzLPZxAoIUGZ90owMVGAQC039KonwHnoq/vXU0CMjAy986qTKZPXwkzRoxJ2BaUqG5PIYU2L8xZ2qd09t+KexhE5AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('266a28bd0c28b669e0c76bb1f1bcffdf')



@app.route("/callback", methods=['POST'])
def callback():

    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)