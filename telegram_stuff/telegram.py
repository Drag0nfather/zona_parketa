import telebot

BOT_API_KEY = 'asdf'
bot = telebot.TeleBot(BOT_API_KEY, parse_mode=None)


def send_messsage_to_telegram_chat(chat_id, name, phone, message):
    message = 'проконсультироваться' if not message else f'"{message}"'
    message_text = (f'Обратная связь с сайта Зона паркета.\n'
                    f'Пользователь {name} ({phone}) хочет {message}')
    bot.send_message(chat_id, message_text)
