# install: line-bot-sdk, flask, pyquery
# command:$ pip install line-bot-sdk flask pyquery

# import flask
from flask import Flask, request, abort
# import linebot related module
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from modules.reply import faq

# reference the following website --Message objects, if anything else need 
# https://github.com/line/line-bot-sdk-python
from linebot.models import (
    MessageEvent,
    TextMessage,
    StickerMessage,
    TextSendMessage,
    StickerSendMessage,
    LocationSendMessage,
    ImageSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
    URIAction,
    CarouselTemplate,
    CarouselColumn
)

# define an instance of flask
app = Flask(__name__)

# the Webhook of LINE is for identifying deleloper
# related address(https://developers.line.me/console/)
CHANNEL_ACCESS_TOKEN = "PdH+eKnsZXqv11HNNUWjPH1grS/UIatUl1CX4OQyveXeVrIfZ8nELQDeRgvxzfkxfVKsdp2rgur+PsD+Cs6aBlFA/FRLYAF5ra58F2aS/G25LwaXBtCCYHMbtJ4T7eB5SyU3IuJ1yFf76rbu6epn4AdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "876bf8ed7cac2dec91c61565085e6a3f"

# ********* X-LINE-SIGNATURE *********
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
@app.route("/", methods=["POST"])
def callback():
    # when LINE send message to chatbot，get X-Line-Signature from header 
    # X-Line-Signature: channel is valid or not
    signature = request.headers["X-Line-Signature"]
    # transfer the obtained body content to text
    body = request.get_data(as_text=True)
    print("[Message is under X-Line-Signature verifying process]")
    # print(body)
    # once verified, transfer the body content to handler
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("[X-LINE-Signature verification failed, Please check whether CHANNEL_SECRET,CHANNEL_ACCESS_TOKEN are correct!]")
        abort(400)
    return 'OK'
# ********* X-LINE-SIGNATURE *********

# Handler for incoming text messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # when a text message comes in
    # event.message.text : message entered by user
    print("*"*30)
    print("[The user enters an message]")
    # print(str(event))
    # get the text by the user
    user_msg = event.message.text
    print(f"The user enters an message「{user_msg}」")
    # prepare the message to be sent back
    #reply = TextSendMessage(text=f"Hi,you're saying「{user_msg}」, right?")
    reply = faq[user_msg]
    
    # send back message
    # if multiple messages need to be replied, use the following
    # line_bot_api.reply_message(token, [Object, Object, ...])
    line_bot_api.reply_message(
        event.reply_token,
        reply)

import os
# if the application is executed
if __name__ == "__main__":
    print("[The server application starts running]")
    # Get the connection port used by the remote environment;
    # If testing on the local side, set to port=5000 by default.
    port = int(os.environ.get('PORT', 5000))
    print(f"[Flask is about to run on the connection port:{port}]")
    print(f"If testing locally, please enter the command to open the test channel: ./ngrok http {port} ")
    # start the application
    # local test uses 127.0.0.1, debug=True
    # Heroku deploy uses 0.0.0.0
    app.run(host="127.0.0.1", port=port, debug=True)
