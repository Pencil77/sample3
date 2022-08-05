import telebot
import os
from flask import Flask, request

TOKEN = os.environ.get("API_KEY")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,'i am born send me a phone number')

@bot.message_handler(func = lambda msg : len(msg.text) > 0)
def main_message(message):
    pn = message.text ; 
    a = "https://t.me/+91"
    b = "https://t.me/"  
    if(len(pn) == 13) : 
        bot.reply_to(message,b+pn)
    elif (len(pn) == 10) :
        bot.reply_to(message , a+pn) 
    else : 
        bot.reply_to(message , "enter the phone number with correct number of digits and without gaps...")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://sample1751-app.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
