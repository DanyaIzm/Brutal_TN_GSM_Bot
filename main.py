from database.db_class import *
from conf.config import *
import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    db = Database()
    

    updater.start_polling()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    main()

