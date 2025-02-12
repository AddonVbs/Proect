from Setings import Token
import telebot

token = Token

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")


bot.polling(none_stop=True, interval=0)