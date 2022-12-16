# telegramBot7

# бот из библиотеки python-telegram-bot
# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Extensions-%E2%80%93-Your-first-Bot

from config import token
from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# создаем объект
updater = Updater(token, use_context=True)

# для более быстрого доступа вводим (объект) локально
dispatcher = updater.dispatcher

# модуль, чтобы знать, когда (и почему) вещи не работают так, как ожидалось
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    # функция, обрабатывающая обновления
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


# Цель состоит в том, чтобы эта функция вызывалась каждый раз, когда бот получает сообщение Telegram, содержащее команду.
# Для этого можно использовать один из предоставленных подклассов и зарегистрировать его в диспетчере:
# /startCommandHandlerHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Добавим еще один обработчик, который прослушивает обычные сообщения.
# Используйте , другой подкласс, чтобы повторить все текстовые сообщения:/startMessageHandlerHandler
def echo(update: Update, context: CallbackContext):
    # бот должен повторять все некомандные сообщения, которые он получает.
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# Мы хотим реализовать команду, которая будет принимать некоторый текст в качестве аргумента и отвечать на него в CAPS.
# Чтобы упростить задачу, можно получить аргументы (как разделенные на пробелы),
# которые были переданы команде в функции обратного вызова:/capslist
def caps(update: Update, context: CallbackContext):
    # Вводим /caps текст и получаем в ответ ТЕКСТ
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
# запускаем бота
updater.start_polling()
