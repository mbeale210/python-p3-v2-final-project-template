from .base import Base, CURSOR, CONN


class Planet(Base):
    table_name = "planets"

    def __init__(self, name, climate, terrain, population, id=None):
        self.id = id
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.population = population

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS planets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                climate TEXT,
                terrain TEXT,
                population INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO planets (name, climate, terrain, population)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.climate, self.terrain, self.population))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE planets
                SET name = ?, climate = ?, terrain = ?, population = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.climate, self.terrain, self.population, self.id))
            CONN.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM planets"
        CURSOR.execute(sql)
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM planets WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None

    def delete(self):
        sql = "DELETE FROM planets WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()