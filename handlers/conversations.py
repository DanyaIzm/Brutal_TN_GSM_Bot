from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters

from database.inserter_class import Inserter
from .not_an_admin_handler import is_admin
from main import db

# Словари для кэша
NEW_DRIVER_INFO = {
        'first_name': '1',
        'last_name': '1',
        'patronymic': '3'
    }
NEW_CAR_INFO = {
    'number': '',
    'info': ''
}
NEW_TN_INFO = {
    '': ''
}
NEW_GSM_INFO = {
    '': ''
}

USER_INPUT = {}


def cancel(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Действие отменено!")
    return ConversationHandler.END


# Добавление нового водителя
def add_driver_start(update, context):
    if not is_admin(update, context):
        return ConversationHandler.END

    USER_INPUT.update({update.effective_chat.id: NEW_DRIVER_INFO})

    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите фамилию водителя")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Для отмены введите /cancel на любом пункте диалога")
    return 'init_last_name'


def add_driver_last_name(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['last_name'] = update.message.text
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите фамилию ещё раз")
        return 'init_last_name'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите имя водителя")
    return 'init_first_name'


def add_driver_first_name(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['first_name'] = update.message.text
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите имя ещё раз")
        return 'init_first_name'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите отчество водителя")
    return 'init_patronymic'


def add_driver_patronymic(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['patronymic'] = update.message.text
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите отчётство ещё раз")
        return 'init_patronymic'

    try:
        inserter = Inserter(db)
        inserter.insert_driver(USER_INPUT[update.effective_chat.id]['last_name'],
                               USER_INPUT[update.effective_chat.id]['first_name'],
                               USER_INPUT[update.effective_chat.id]['patronymic'])
        del USER_INPUT[update.effective_chat.id]
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Не удалось добавить информацию в базу данных")
        return ConversationHandler.END

    context.bot.send_message(chat_id=update.effective_chat.id, text="Информация успешно добавлена")
    return ConversationHandler.END
