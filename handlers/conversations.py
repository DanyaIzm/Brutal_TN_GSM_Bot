from telegram.ext import ConversationHandler, MessageHandler, CommandHandler, Filters

from database.inserter_class import Inserter
from .not_an_admin_handler import is_admin
from database.selector_class import Selector
from exceptions.exceptions import NoInfoInDatabaseException
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
    'tn_date': '',
    'shift': '',
    'driver_ln': '',
    'car_number': '',
    'tn': '',
    'cost': '',
    'info': ''
}
NEW_GSM_INFO = {
    'gsm_date': '',
    'shift': '',
    'driver_ln': '',
    'car_number': '',
    'gsm': '',
    'cost': '',
    'info': ''
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


# Добавить ТН
def add_tn_start(update, context):
    if not is_admin(update, context):
        return ConversationHandler.END

    USER_INPUT.update({update.effective_chat.id: NEW_TN_INFO})

    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите дату ТН в формате DD.MM.YY")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Для отмены введите /cancel на любом пункте диалога")
    return 'init_tn_date'


def add_tn_date(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['tn_date'] = update.message.text
        date = update.message.text.split('.')

        # Проверка на правильность введённой даты
        if len(date) != 3:
            raise Exception
        int(date[0])
        int(date[1])
        int(date[2])

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите дату ещё раз")
        return 'init_tn_date'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите смену")
    return 'init_shift'


def add_tn_shift(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['shift'] = update.message.text

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите смену ещё раз")
        return 'init_shift'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите фамилию водителя")
    return 'init_driver_ln'


def add_tn_driver_ln(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['driver_ln'] = update.message.text

        selector = Selector(db)
        fetch = selector.sql_query(f"SELECT last_name FROM drivers WHERE last_name = '{update.message.text}'")
        if not fetch:
            raise NoInfoInDatabaseException

    except NoInfoInDatabaseException:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Водителя нет в базе данных.\n\n"
                                                                        "Введите фамилию ещё раз")
        return 'init_driver_ln'

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите фамилию ещё раз")
        return 'init_driver_ln'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите номер машины")
    return 'init_car_number'


def add_tn_car_number(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['car_number'] = update.message.text

        selector = Selector(db)
        fetch = selector.sql_query(f"SELECT number FROM cars WHERE number = '{update.message.text}'")
        if not fetch:
            raise NoInfoInDatabaseException

    except NoInfoInDatabaseException:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Номера нет в базе данных.\n\n"
                                                                        "Введите номер ещё раз")
        return 'init_car_number'

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите номер ещё раз")
        return 'init_car_number'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите количество ТН")
    return 'init_tn'


def add_tn_tn(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['tn'] = update.message.text
        int(update.message.text)

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите колчество тн ещё раз")
        return 'init_tn'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите стоимость")
    return 'init_cost'


def add_tn_cost(update, context):
    try:
        USER_INPUT[update.effective_chat.id]['cost'] = update.message.text
        int(update.message.text)

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Произошла ошибка.\n"
                                                                        "Данные введены некорректно.\n\n"
                                                                        "Введите стоимость ещё раз")
        return 'init_cost'

    context.bot.send_message(chat_id=update.effective_chat.id, text="Теперь введите дополнительную информацию")
    return 'init_info'


def add_tn_info(update, context):
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
        inserter.insert_tn(USER_INPUT[update.effective_chat.id]['tn_date'],
                           USER_INPUT[update.effective_chat.id]['shift'],
                           USER_INPUT[update.effective_chat.id]['driver_ln'],
                           USER_INPUT[update.effective_chat.id]['car_number'],
                           int(USER_INPUT[update.effective_chat.id]['tn']),
                           int(USER_INPUT[update.effective_chat.id]['cost']),
                           USER_INPUT[update.effective_chat.id]['info'])
        del USER_INPUT[update.effective_chat.id]
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Не удалось добавить информацию в базу данных")
        return ConversationHandler.END

    context.bot.send_message(chat_id=update.effective_chat.id, text="Информация успешно добавлена")
    return ConversationHandler.END
