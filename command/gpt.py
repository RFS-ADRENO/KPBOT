import openai
from action.sendMessage import sendMessage
from action.seen import seen
def gpt(sender_id, message):
            seen(sender_id)
            msg=message[5:len(message)]
            openai.api_key = "ở đây là token chatgpt"
            res = openai.Completion.create(
                model='text-davinci-003',
                prompt=msg,
                max_tokens=4000,
                temperature=0
            )
            res = res.choices[0].text
            sendMessage(sender_id, res)
