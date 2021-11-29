from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters

from .commands import *
from .conversation_handers import *
from .messages import *


def add_handlers(dispatcher):
    # Команды
    start_handler = CommandHandler('start', start_message)
    dispatcher.add_handler(start_handler)

    # Сообщения
    query_message_handler = MessageHandler(Filters.regex('Запросы'), message_query)
    dispatcher.add_handler(query_message_handler)

    # Диалоги
    dispatcher.add_handler(add_driver_conversation_handler)

    # TODO: Добавить ответ на остальные сообщения!!!
