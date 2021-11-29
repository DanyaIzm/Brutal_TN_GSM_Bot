from main import db
from keyboards.keyboards import *
from .not_an_admin_handler import is_admin


# Ответ на неизвестную команду/сообщение
def unknown_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, я вас не понимаю =(")


# Сообщение с кнопками запросов
def message_query(update, context):
    if not is_admin(update, context):
        return
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здесь вы можете выбрать необходимые запросы!",
                             reply_markup=message_query_inline_markup())
