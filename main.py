from database.db_class import *
from conf.config import *
from keyboards.keyboards import *
from handlers.handlers import *
import logging
from telegram.ext import Updater

db = Database()

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    add_handlers(dispatcher)
    updater.start_polling()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    main()

