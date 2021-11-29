from telegram.ext import ConversationHandler

from main import db


# Сообщение на ответ об отсутствии админки
def no_admin_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вы не имеете прав администратора!")
    return False


def is_admin(update, context):
    if not db.check_if_admin(update.effective_chat.id):
        return no_admin_message(update, context)