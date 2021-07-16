from random import randint, choice
from requests import get
from bs4 import BeautifulSoup
from threading import Timer
import telebot

API_TOKEN = '1879648757:AAG0i16nDsQw3cB6NAxsEESxqHcf54yOmzg'

bot = telebot.TeleBot(API_TOKEN)
global chat_id

@bot.message_handler(commands=['start'])
# def send_compliment(message):
#     chat_id = message.chat.id
#     # print(get_rand_compliment())
#     bot.send_message(chat_id, get_rand_compliment())

# def compliment_ddos(chat_id):
#     Timer(30.0,compliment_ddos).start()
#     bot.send_message(chat_id, get_rand_compliment())
#     compliment_ddos(chat_id)
def send_compliment(message):
    Timer(8640.0,send_compliment).start()
    bot.send_message(message.chat.id, get_rand_compliment())
    send_compliment(message)

def get_rand_compliment():
        random_page_number = str(randint(1,17))
        webpage = get('http://kompli.me/krasivye-slova-dlya-devushek/page/' + random_page_number).text
        tags = BeautifulSoup(webpage,'html.parser').\
            find_all('a')
        compliments = []
        for tag in tags:
            tag_text = tag.get_text()
            if tag.text == 'Назад':
                break
            compliments.append(tag_text)

        return choice(compliments[4:])

bot.polling(none_stop=True)
# send_compliment()

# h350yam 2021
