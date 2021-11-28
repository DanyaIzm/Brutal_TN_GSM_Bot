from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters

from .commands import *
from .conversations import *
from .messages import *


def add_handlers(dispatcher):
    start_handler = CommandHandler('start', start_message)
    dispatcher.add_handler(start_handler)
    query_message_handler = MessageHandler(Filters.regex('Запросы'), message_query)
    dispatcher.add_handler(query_message_handler)
