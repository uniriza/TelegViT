import telebot
from telebot import types
token = '6034053467:AAFQKwgRvbTAYPdLRD4G1SVNmRThwadxnd8'
client = telebot.TeleBot(token)
@client.message_handler(content_types=['text'])
def get_text(message):
    client.send_message(message.chat.id, 'ska')


client.polling(non_stop=True)
