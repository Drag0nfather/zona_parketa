import os

import telebot
from dotenv import load_dotenv


load_dotenv()

BOT_API_KEY = os.environ.get('TELEGRAM_API_KEY')
bot = telebot.TeleBot(BOT_API_KEY, parse_mode=None)


def send_messsage_to_telegram_chat(chat_id, name, phone, message):
    if not message:
        message_text = (f'Обратная связь с сайта Зона паркета.\n'
                        f'Пользователь {name} {phone} хочет проконсультироваться')
    else:
        message_text = (f'Обратная связь с сайта Зона паркета.\n'
                        f'Пользователь {name} {phone} хочет узнать: \n"{message}"')
    bot.send_message(chat_id, message_text)


def handle_senddoc(chat_id, name, phone, file):
    bot.send_document(
        chat_id,
        file,
        caption=f'Пользователь {name}, {phone} сделал расчет сметы на сайте',
        visible_file_name="smeta.docx"
    )
