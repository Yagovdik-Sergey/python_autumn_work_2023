import datetime
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import json


# Загрузка контактов из файла (заменить путь на свой)
def load_contacts(file_path):
    try:
        with open(file_path, 'r') as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return {}


# Отправка поздравления
def send_birthday_greeting(bot: Bot, chat_id: int, name: str):
    greeting_message = f"С Днем Рождения, {name}! 🎉🎂"
    bot.send_message(chat_id, greeting_message)


# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я бот для отправки поздравлений по дню рождения. '
                              'Для остановки введите /stop.')


# Обработчик команды /stop
def stop(update: Update, context: CallbackContext):
    update.message.reply_text('Бот остановлен.')
    context.job_queue.stop()


# Обработчик дня рождения
def birthday_handler(context: CallbackContext):
    job = context.job
    chat_id = job.context['chat_id']
    name = job.context['name']
    send_birthday_greeting(context.bot, chat_id, name)


# Главная функция
def main():
    # Заменить 'YOUR_BOT_TOKEN' на токен вашего бота
    bot_token = 'YOUR_BOT_TOKEN'
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    # Добавление обработчика команды /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Добавление обработчика команды /stop
    stop_handler = CommandHandler('stop', stop)
    dispatcher.add_handler(stop_handler)

    # Загрузка контактов из файла (замените путь на свой)
    contacts_file_path = 'contacts.json'
    contacts = load_contacts(contacts_file_path)

    # Установка таймеров для отправки поздравлений
    for chat_id, contact_info in contacts.items():
        birthday_date = datetime.datetime.strptime(contact_info['birthday'], '%Y-%m-%d').date()
        today = datetime.date.today()

        if birthday_date == today:
            name = contact_info['name']
            job_context = {'chat_id': int(chat_id), 'name': name}
            updater.job_queue.run_once(birthday_handler, when=0, context=job_context)

    # Запуск бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
