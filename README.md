# telegramBot7

#### Бот из библиотеки python-telegram-bot

* Команда: /start - ответ: I'm a bot, please talk to me!
* Бот повторяет все некомандные сообщения, которые он получает.
* Вводим /caps текст и получаем в ответ ТЕКСТ

#### https://github.com/python-telegram-bot/v13.x-wiki/wiki/Extensions-%E2%80%93-Your-first-Bot

## Требования:

#### Создаем файл config.py, в котором записываем токен в виде:

```python
# тестовый токен
token = "59******2:AAE*****************************Ny-Q"
```

## Подключаем библиотеки:

```python
from config import token
from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
```

## Примеры использования:

#### Запускаем бота

```python
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher
```

#### Модуль, чтобы знать, когда (и почему) вещи не работают так, как ожидалось

```python
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
```

#### Функция, обрабатывающая команду /start

```python
def start(update: Update, context: CallbackContext):
    # функция, обрабатывающая команду /start
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
```

#### Цель состоит в том, чтобы эта функция вызывалась каждый раз, когда бот получает сообщение Telegram, содержащее команду. Для этого можно использовать один из предоставленных подклассов и зарегистрировать его в диспетчере: /startCommandHandlerHandler

```python
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
```

#### бот должен повторять все некомандные сообщения, которые он получает.

```python
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
```

#### Вводим /caps и через пробел - текст и получаем в ответ ТЕКСТ

```python
def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
```

#### Запускаем бота

```python
updater.start_polling()
```