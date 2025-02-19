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
    btn2 = types.KeyboardButton("Мой Акаунт💠")
    btn3 = types.KeyboardButton("Помощь ☎")
    markup.add(btn2,btn3)
    bot.send_message(message.chat.id, "👾Добро пожаловать👾\nEсли вы еще не зарегистрировались, то нажмите на кнопку Помощь ☎".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "Помощь ☎":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Mabtn2 = types.KeyboardButton("Зарегестрироватья🔑")
        Mabtn3 = types.KeyboardButton("Ошибка ⚠")
        markup.add(Mabtn2,Mabtn3)
        bot.send_message(message.chat.id, "Чем могу помочь ?".format(message.from_user), reply_markup=markup)
    if message.text == "Мой Акаунт💠":
        









# if message.text == "Ошибка ⚠":
#     bot.send_message(message.chat.id, "Напишите вашу проблему", reply_markup=types.ReplyKeyboardRemove())
    







bot.polling(none_stop=True, interval=0)
