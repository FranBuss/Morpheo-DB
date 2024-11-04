import pyodbc

class DatabaseManager:

    def __init__(self):
        self.conn = pyodbc.connect("DRIVER={SQL Server};SERVER=DESKTOP-1AMST2L\\SQLEXPRESS;DATABASE=MORPHEO-DB")
        self.cursor = self.conn.cursor()

    def select_data(self, sql_string):
        self.cursor.execute(sql_string)
        table_data = self.cursor.fetchall()
        return table_data

    def insert_data(self, sql_string, data):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_string, data)
            cursor.commit()
            return 0
        except pyodbc.Error as ex:
            print('ERROR : ' + str(ex))
            return 1

    def close_conn(self):
        self.conn.close()