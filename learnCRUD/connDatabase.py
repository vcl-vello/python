import psycopg2
from pprint import pprint

class DatabaseConnection:
    def __init__ (self) :
        try:
            self.connection = psycopg2.connect(
                "dbname='test' user='vello' host='localhost' password='123' port='5432' options='-c search_path=python1'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint('cannot connect to database')

    def insert_new_record(self):
        new_record = ("SKU000020002","Item ke 2","20000")
        insert_command = "INSERT INTO product VALUES ('" + new_record[0] + "','" + new_record[1] + "'," + new_record[2] + ")"
        pprint(insert_command)
        self.cursor.execute(insert_command)


database_connection = DatabaseConnection()
database_connection.insert_new_record()