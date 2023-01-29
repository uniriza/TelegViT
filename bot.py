import telebot
from telebot import types




token = '6034053467:AAFQKwgRvbTAYPdLRD4G1SVNmRThwadxnd8'
client = telebot.TeleBot(token)
@client.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    one_button = types.KeyboardButton("POSRAT")
    markup.add(one_button)
    client.send_message(message.chat.id, text="", reply_markup=markup)
@client.message_handler(content_types=['text'])
def func(message):
    if(message.text == "POSRAT"):





client.polling(non_stop=True)
