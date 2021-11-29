from database.db_class import *


class Selector(IDatabase):

    def __init__(self, db: Database):
        self._connection = db._connection
        self._cursor = db._cursor

    def sql_query(self, query):
        self._cursor.execute(query)
        self._connection.commit()
        return self._cursor.fetchall()
