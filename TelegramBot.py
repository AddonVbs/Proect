from Setings import Token
import telebot
from telebot import types
import sqlite3
import datetime

token = Token

bot = telebot.TeleBot(token)

DB_PATH = "tasks.db"

@bot.message_handler(content_types=['text'])
def strat(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Зарегестрироваться 🔑")
        btn2 = types.KeyboardButton("Изменить пароль⚙️")
        btn3 = types.KeyboardButton("Помощь🌌")
        markup.add(btn1,btn2,btn3)

def get_tasks_for_today():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("SELECT id, task, status FROM tasks WHERE date=?", (today,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks
    






bot.polling(none_stop=True, interval=0)
