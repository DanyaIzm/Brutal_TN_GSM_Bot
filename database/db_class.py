from .IDatabase import *


# Класс для работы с базой данных
class Database(IDatabase):

    def __init__(self):
        create_users_query = "CREATE TABLE IF NOT EXISTS users " \
                             "(id NUMBER, username TEXT, last_name TEXT, first_name TEXT, status BOOL, " \
                             "PRIMARY KEY(id))"

        create_car_query = "CREATE TABLE IF NOT EXISTS cars " \
                           "(number TEXT, info TEXT, " \
                           "PRIMARY KEY(number) )"

        create_driver_query = "CREATE TABLE IF NOT EXISTS drivers " \
                              "(last_name TEXT, first_name TEXT, patronymic TEXT, " \
                              "PRIMARY KEY(last_name) )"

        create_tn_query = "CREATE TABLE IF NOT EXISTS tn " \
                          "(tn_date TEXT, shift TEXT, driver_ln TEXT, " \
                          "car_number TEXT, tn NUMBER, cost NUMBER, info TEXT, " \
                          "PRIMARY KEY(tn_date, shift, driver_ln), " \
                          "FOREIGN KEY(driver_ln) REFERENCES drivers(last_name), " \
                          "FOREIGN KEY(car_number) REFERENCES cars(number))"

        create_gsm_query = "CREATE TABLE IF NOT EXISTS gsm " \
                           "(gsm_date TEXT, shift TEXT, driver_ln TEXT, " \
                           "car_number TEXT, gsm NUMBER, cost NUMBER, info TEXT, " \
                           "PRIMARY KEY(gsm_date, shift, driver_ln), " \
                           "FOREIGN KEY(driver_ln) REFERENCES drivers(last_name), " \
                           "FOREIGN KEY(car_number) REFERENCES cars(number))"

        self._cursor.execute(create_users_query)
        self._connection.commit()
        self._cursor.execute(create_car_query)
        self._connection.commit()
        self._cursor.execute(create_driver_query)
        self._connection.commit()
        self._cursor.execute(create_tn_query)
        self._connection.commit()
        self._cursor.execute(create_gsm_query)
        self._connection.commit()

    def check_if_admin(self, user_id):
        check_query = f"SELECT status FROM users WHERE id = '{int(user_id)}'"
        self._cursor.execute(check_query)

        if self._cursor.fetchone()[0] == 1:
            return True
        else:
            # сообщение
            return False

    def check_new_user(self, id, username, last_name, first_name):
        check_query = f"SELECT * FROM users WHERE id = '{int(id)}'"
        self._cursor.execute(check_query)

        if not self._cursor.fetchone():
            if self.insert_user(id, username, last_name, first_name) == "ok":
                return "ok"
            else:
                return "Ошибка"

    def insert_user(self, id, username, last_name, first_name):
        insert_query = f"INSERT INTO users(id, username, last_name, first_name, status) " \
                       f"VALUES ({id}, '{username}', '{last_name}', '{first_name}', 0)"

        try:
            self._cursor.execute(insert_query)
            self._connection.commit()
            return "ok"
        except Exception as e:
            print(e)
            return "Ошибка"
