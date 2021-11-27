from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters
from main import *


def no_admin_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вы не имеете прав администратора!")


def start_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте!")
    if db.check_new_user(update.effective_chat.id, update.effective_chat.username,
                         update.effective_chat.last_name, update.effective_chat.first_name) == "ok":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать в телеграм бота!")
    if db.check_if_admin(update.effective_chat.id):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите пункт меню: ",
                                 reply_markup=message_start_markup())
    else:
        no_admin_message(update, context)


def message_query(update, context):
    if not db.check_if_admin(update.effective_chat.id):
        return no_admin_message(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здесь вы можете выбрать необходимые запросы!",
                             reply_markup=message_query_inline_markup())


def add_handlers(dispatcher):
    start_handler = CommandHandler('start', start_message)
    dispatcher.add_handler(start_handler)
    query_message_handler = MessageHandler(Filters.regex('Запросы'), message_query)
    dispatcher.add_handler(query_message_handler)
