import sqlite3


class IDatabase:
    _connection = sqlite3.connect("database/main_db.db", check_same_thread=False)
    _cursor = _connection.cursor()
