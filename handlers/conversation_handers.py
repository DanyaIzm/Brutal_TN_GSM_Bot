from .conversations import *


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
