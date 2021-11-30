from database.db_class import *


class Inserter(IDatabase):

    def __init__(self, db: Database):
        self._connection = db._connection
        self._cursor = db._cursor

    def insert_car(self, number, info):
        insert_query = f"INSERT INTO cars(number, info) VALUES ('{number}', '{info}')"

        self._cursor.execute(insert_query)
        self._connection.commit()
        return "ok"

    def insert_driver(self, last_name, first_name, patronymic):
        insert_query = f"INSERT INTO drivers(last_name, first_name, patronymic) VALUES " \
                       f"('{last_name}', '{first_name}', '{patronymic}')"

        self._cursor.execute(insert_query)
        self._connection.commit()
        return "ok"

    def insert_tn(self, tn_date, shift, driver_ln, car_number, tn, cost, info):
        insert_query = f"INSERT INTO tn(tn_date, shift, driver_ln, car_number, tn, cost, info) " \
                       f"VALUES ('{tn_date}', '{shift}', '{driver_ln}', '{car_number}', '{tn}', '{cost}', '{info}')"

        self._cursor.execute(insert_query)
        self._connection.commit()
        return "ok"

    def insert_gsm(self, gsm_date, shift, driver_ln, car_number, gsm, cost, info):
        insert_query = f"INSERT INTO tn(gsm_date, shift, driver_ln, car_number, gsm, cost, info) " \
                       f"VALUES ('{gsm_date}', '{shift}', '{driver_ln}', '{car_number}', '{gsm}', '{cost}', '{info}')"

        self._cursor.execute(insert_query)
        self._connection.commit()
        return "ok"
