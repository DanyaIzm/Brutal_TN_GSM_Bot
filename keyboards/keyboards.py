from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def message_start_markup():
    button_list = [
        ['Запросы'],
        ['Добавить ТН'],
        ['Добавить ГСМ'],
        ['Добавить водителя'],
        ['Добавить машину']
    ]
    return ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=button_list)


def message_query_inline_markup():
    keyboard = [
        [InlineKeyboardButton("Запрос1", callback_data='1')],
        [InlineKeyboardButton("Запрос2", callback_data='2')],
        [InlineKeyboardButton("Запрос3", callback_data='3')],
        [InlineKeyboardButton("Запрос4", callback_data='4')],
        [InlineKeyboardButton("Запрос5", callback_data='5')],
    ]
    return InlineKeyboardMarkup(keyboard)