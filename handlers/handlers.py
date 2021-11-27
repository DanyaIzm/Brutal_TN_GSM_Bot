from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters
from main import db, updater, dispatcher


def start_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте!")
    if db.check_new_user(update.effective_chat.id, update.effective_chat.username,
                         update.effective_chat.last_name, update.effective_chat.first_name) == "ok":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать в телеграм бота!")
    if db.check_if_admin(update.effective_chat.id):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите пункт меню: ")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Вы не имеете прав администратора!")


def add_handlers():
    start_handler = CommandHandler('start', start_message)
    dispatcher.add_handler(start_handler)