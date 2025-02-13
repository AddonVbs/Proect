from Setings import Token
import telebot
from telebot import types

token = Token

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def strat(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зарегестрироваться 🔑")
        btn2 = types.KeyboardButton("Изменить пароль⚙️")
        btn3 = types.KeyboardButton("Помощь🌌")
        markup.add(btn1,btn2,btn3)
        






bot.polling(none_stop=True, interval=0)
