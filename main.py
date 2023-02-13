import requests
import threading
from flask import Flask, request
from command.help import help
from command.covid import covid
from command.diche import diche
from command.dichv import dichv
from command.wiki import wiki
from command.fact import fact
from command.sim import sim
from command.gpt import gpt
app = Flask(__name__)
from sanic import response
# Adds support for GET requests to our webhook
@app.route('/', methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")== "<verify token>":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200
@app.route("/", methods=['POST'])
def fbwebhook():
   data_user=request.get_json()
   for event in data_user['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                sender_id = message['sender']['id']
                message_text = message["message"]["text"]
                if any(["/wiki" in message_text.lower()]):
                     thread1 = threading.Thread(target=wiki, args=(sender_id, message_text))
                     thread1.start()
                elif any(["/help" in message_text.lower()]):
                     thread1 = threading.Thread(target=help, args=(sender_id, message_text))
                     thread1.start()
                elif any(["/covid" in message_text.lower()]):
                     thread1 = threading.Thread(target=covid, args=(sender_id, message_text))
                     thread1.start()
                elif any(["/diche" in message_text.lower()]):
                     thread1 = threading.Thread(target=diche, args=(sender_id, message_text))
                     thread1.start()
                elif any(["/dichv" in message_text.lower()]):
                     thread1 = threading.Thread(target=dichv, args=(sender_id, message_text))
                     thread1.start()
                elif any(["/fact" in message_text.lower()]):
                     thread1 = threading.Thread(target=fact, args=(sender_id, message_text))
                     thread1.start()
                elif any(["/gpt" in message_text.lower()]):
                     thread1 = threading.Thread(target=gpt, args=(sender_id, message_text))
                     thread1.start()
                else:
                     thread1 = threading.Thread(target=sim, args=(sender_id, message_text))
                     thread1.start()

                
                
   return "Message Processed"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)