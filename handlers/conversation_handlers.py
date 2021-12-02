from .conversations import *


# SQL команда
sql_query_conversation_handler = ConversationHandler(
    entry_points=[
        CommandHandler('sql', sql_query_start)
    ],
    states={
        'init_sql_query': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, sql_query_execute)
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)


# Добавить нового водителя
add_driver_conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('Добавить водителя'), add_driver_start)
    ],
    states={
        'init_last_name': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_driver_last_name)
        ],
        'init_first_name': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_driver_first_name)
        ],
        'init_patronymic': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_driver_patronymic)
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)


# Добавить новую машину
add_car_conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('Добавить машину'), add_car_start)
    ],
    states={
        'init_number': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_car_number)
        ],
        'init_info': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_car_info)
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)


# Добавить тн
add_tn_conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('Добавить ТН'), add_tn_start)
    ],
    states={
        'init_tn_date': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_tn_date)
        ],
        'init_shift': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_tn_shift)
        ],
        'init_driver_ln': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_tn_driver_ln)
        ],
        'init_car_number': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_tn_car_number)
        ],
        'init_tn': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_tn_tn)
        ],
        'init_cost': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_tn_cost)
        ],
        'init_info': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_tn_info)
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)


# Добавить гсм
add_gsm_conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('Добавить ГСМ'), add_gsm_start)
    ],
    states={
        'init_gsm_date': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_gsm_date)
        ],
        'init_shift': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_gsm_shift)
        ],
        'init_driver_ln': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_gsm_driver_ln)
        ],
        'init_car_number': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_gsm_car_number)
        ],
        'init_gsm': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_gsm_gsm)
        ],
        'init_cost': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_gsm_cost)
        ],
        'init_info': [
            CommandHandler('cancel', cancel),
            MessageHandler(Filters.text, add_gsm_info)
        ]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)
