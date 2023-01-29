import telebot
import requests
import time
from bs4 import BeautifulSoup
from telebot import types



token = '6034053467:AAFQKwgRvbTAYPdLRD4G1SVNmRThwadxnd8'
client = telebot.TeleBot(token)
@client.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    one_button = types.KeyboardButton("POSRAT")
    markup.add(one_button)
    client.send_message(message.chat.id, text="kek", reply_markup=markup)

@client.message_handler(content_types=['text'])
def func(message):
    if(message.text == 'POSRAT'):
            url_to_crawl = "https://vk.com/superfezdgjik"
            response = requests.get(url_to_crawl)
            soup = BeautifulSoup(response.text, "lxml")
            lala = soup.title
            client.send_message(message.chat.id, text=str(lala))




client.polling(non_stop=True)
