# import
import requests
from bs4 import BeautifulSoup as b
import random
import telebot

# =====================================PARSE=======================================#

URL = 'https://www.anekdot.ru/random/anekdot/'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

# =====================================TG BOT======================================#

TOKEN = ""  # bot token

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, чтобы получить анекдот введи любую цифру:')


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '0123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введи любую цифру:')


if __name__ == '__main__':
    bot.infinity_polling()
