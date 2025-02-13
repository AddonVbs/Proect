from Setings import Token
import telebot
from telebot import types
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


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

tasks = [
    {"id": 1, "task": "Сделать зарядку", "date": "2025-02-13", "status": "🕒 В процессе"},
    {"id": 2, "task": "Прочитать 10 страниц книги", "date": "2025-02-13", "status": "🕒 В процессе"},
    {"id": 3, "task": "Изучить Python 30 минут", "date": "2025-02-14", "status": "🕒 В процессе"},
]

# Функция для получения задач на сегодня
def get_tasks_for_today():
    today = datetime.today().strftime('%Y-%m-%d')
    return [t for t in tasks if t["date"] == today]

# Функция для получения задач за год
def get_tasks_for_year():
    year = datetime.today().strftime('%Y')
    return [t for t in tasks if t["date"].startswith(year)]

# Функция для изменения статуса задачи
def update_task_status(task_id, new_status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            return True
    return False

# Генерация кнопок для задач
def generate_task_buttons(task_list):
    markup = InlineKeyboardMarkup()
    for task in task_list:
        btn_text = f"{task['task']} - {task['status']}"
        btn = InlineKeyboardButton(btn_text, callback_data=f"task_{task['id']}")
        markup.add(btn)
    return markup

# Команда /today
@bot.message_handler(commands=['today'])
def send_today_tasks(message):
    today_tasks = get_tasks_for_today()
    if today_tasks:
        bot.send_message(message.chat.id, "Ваши задачи на сегодня:", reply_markup=generate_task_buttons(today_tasks))
    else:
        bot.send_message(message.chat.id, "На сегодня задач нет.")

# Команда /year
@bot.message_handler(commands=['year'])
def send_year_tasks(message):
    year_tasks = get_tasks_for_year()
    if year_tasks:
        bot.send_message(message.chat.id, "Ваши задачи за год:", reply_markup=generate_task_buttons(year_tasks))
    else:
        bot.send_message(message.chat.id, "За год задач нет.")

# Обработчик кнопок (изменение статуса)
@bot.callback_query_handler(func=lambda call: call.data.startswith("task_"))
def handle_task_callback(call):
    task_id = int(call.data.split("_")[1])
    if update_task_status(task_id, "✅ Выполнено"):
        bot.answer_callback_query(call.id, "Задача отмечена как выполненная.")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="✅ Задача выполнена!")
    else:
        bot.answer_callback_query(call.id, "Ошибка: задача не найдена.")






bot.polling(none_stop=True, interval=0)
