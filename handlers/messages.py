from main import db
from keyboards.keyboards import *


# Сообщение на ответ об отсутствии админки
def no_admin_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вы не имеете прав администратора!")


# Ответ на неизвестную команду/сообщение
def unknown_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, я вас не понимаю =(")


def message_query(update, context):
    if not db.check_if_admin(update.effective_chat.id):
        return no_admin_message(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здесь вы можете выбрать необходимые запросы!",
                             reply_markup=message_query_inline_markup())
