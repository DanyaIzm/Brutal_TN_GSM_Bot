from main import db
from keyboards.keyboards import *


def no_admin_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вы не имеете прав администратора!")


def message_query(update, context):
    if not db.check_if_admin(update.effective_chat.id):
        return no_admin_message(update, context)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здесь вы можете выбрать необходимые запросы!",
                             reply_markup=message_query_inline_markup())
