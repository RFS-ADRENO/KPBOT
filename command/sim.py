import requests, json
from action.sendMessage import sendMessage
from action.seen import seen
def sim(sender_id, message):
    seen(sender_id)
    res = requests.get(f"https://api.simsimi.net/v2/?text={message}&lc=vn").json()
    sendMessage(sender_id, res["success"])