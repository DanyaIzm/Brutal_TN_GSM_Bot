from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters

from .commands import *
from .conversation_handlers import *
from .messages import *


def add_handlers(dispatcher):
    # Команды
    start_handler = CommandHandler('start', start_message)
    dispatcher.add_handler(start_handler)

    # Сообщения
    query_message_handler = MessageHandler(Filters.regex('Запросы'), message_query)
    dispatcher.add_handler(query_message_handler)

    # Диалоги
    dispatcher.add_handler(sql_query_conversation_handler)
    dispatcher.add_handler(add_driver_conversation_handler)
    dispatcher.add_handler(add_car_conversation_handler)
    dispatcher.add_handler(add_tn_conversation_handler)
    dispatcher.add_handler(add_gsm_conversation_handler)

    # Ответ на неизвестные сообщения
    unknown_command_handler = MessageHandler(Filters.text, unknown_command)
    dispatcher.add_handler(unknown_command_handler)
