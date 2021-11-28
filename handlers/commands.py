from main import db
from keyboards.keyboards import *
from .messages import no_admin_message


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