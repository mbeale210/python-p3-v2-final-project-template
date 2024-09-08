import sqlite3
from lib.debug import debug

CONN = sqlite3.connect('star_wars.db')
CURSOR = CONN.cursor()

class Base:
    table_name = ""

    @classmethod
    def drop_table(cls):
        sql = f"DROP TABLE IF EXISTS {cls.table_name}"
        CURSOR.execute(sql)
        CONN.commit()