from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters

from database.inserter_class import Inserter
from .not_an_admin_handler import is_admin
from database.selector_class import Selector
from main import db

# Словари для кэша
NEW_DRIVER_INFO = {
    'first_name': '',
    'last_name': '',
    'patronymic': ''
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


# SQL запрос
def sql_query_start(update, context):
    if not is_admin(update, context):
        return ConversationHandler.END

    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите запрос")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Для отмены введите /cancel на любом пункте диалога")
    return 'init_sql_query'


def sql_query_execute(update, context):
    sql_query_text = update.message.text

    try:
        selector = Selector(db)
        fetch = selector.sql_query(sql_query_text)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Запрос успешно выполнен")
        if fetch is None:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Нет текта ответа от БД")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"{fetch}")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Не удалось выполнить запрос")
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{e}")
    finally:
        return ConversationHandler.END


# Добавление нового водителя
def add_driver_start(update, context):
    if not is_admin(update, context):
        return ConversationHandler.END

    USER_INPUT.update({update.effective_chat.id: NEW_DRIVER_INFO})

    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите фамилию водителя")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Для отмены введите /cancel на любом пункте диалога")
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


# Добавить новую машину
def add_car_start(update, context):
    if not is_admin(update, context):
        return ConversationHandler.END

    USER_INPUT.update({update.effective_chat.id: NEW_CAR_INFO})

    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите номер машины")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Для отмены введите /cancel на любом пункте диалога")
    return 'init_number'


def add_car_number(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['number'] = update.message.text
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите номер ещё раз")
        return 'init_number'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите информацию о машине")
    return 'init_info'


def add_car_info(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['info'] = update.message.text
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите информацию ещё раз")
        return 'init_info'

    try:
        inserter = Inserter(db)
        inserter.insert_car(USER_INPUT[update.effective_chat.id]['number'],
                            USER_INPUT[update.effective_chat.id]['info'])
        del USER_INPUT[update.effective_chat.id]
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Не удалось добавить информацию в базу данных")
        return ConversationHandler.END

    context.bot.send_message(chat_id=update.effective_chat.id, text="Информация успешно добавлена")
    return ConversationHandler.END
