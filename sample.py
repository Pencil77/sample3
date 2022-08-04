import telebot
bot = telebot.TeleBot('5433650120:AAFw-NJ8I6Gr-6xnJtxnXvEHe0kA8U1H0sk')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,'i am born send me a phone number')

@bot.message_handler(func = lambda msg : len(msg.text) == 10)
def start_message(message):
    pn = message.text ; 
    a = "https://t.me/+91"
    b = "https://t.me/"  
    f = ""
    if(len(pn) == 13) : 
        bot.reply_to(message,b+pn)
    elif (len(pn) == 10) :
        bot.reply_to(message , a+pn) 
    else : 
        bot.reply_to(message , "enter the phone number with correct number of digits and without gaps...")

bot.polling()