from Setings import Token
import telebot
from telebot import types
import datetime

token = Token

bot = telebot.TeleBot(token)

DB_PATH = "tasks.db"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Мой Акаунт")
    btn3 = types.KeyboardButton("Помощь")
    markup.add(btn2,btn3)
    bot.send_message(message.chat.id, "👾Добро пожаловать👾\nEсли вы еще не зарегистрировались, то нажмите на кнопку Зарегестрироваться 🔑".format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True, interval=0)
