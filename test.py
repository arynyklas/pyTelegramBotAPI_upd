import telebot
import logging


logger = telebot.logger

telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot('1278417528:AAFQeXujjPYiDtR7_e4xwcnLnrsK53zTVr0')


@bot.middleware_handler(update_types=['message'])
def middleware(bot_instance, message):
    print(type(bot_instance))

@bot.message_handler(content_types=['text'])
def text(message, *args):
    print(1)
    print(*args)


bot.polling()