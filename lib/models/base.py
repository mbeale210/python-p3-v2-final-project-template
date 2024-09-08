from . import CONN, CURSOR

class Base:
    table_name = ""

    @classmethod
    def drop_table(cls):
        sql = f"DROP TABLE IF EXISTS {cls.table_name}"
        CURSOR.execute(sql)
        CONN.commit()