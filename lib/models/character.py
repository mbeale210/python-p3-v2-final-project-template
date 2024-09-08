from .base import Base, CONN, CURSOR
from .planet import Planet

class Character(Base):
    table_name = "characters"

    def __init__(self, name, species, birth_year, planet_id, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.birth_year = birth_year
        self.planet_id = planet_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                birth_year TEXT,
                planet_id INTEGER,
                FOREIGN KEY (planet_id) REFERENCES planets(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO characters (name, species, birth_year, planet_id)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.species, self.birth_year, self.planet_id))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE characters
                SET name = ?, species = ?, birth_year = ?, planet_id = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.name, self.species, self.birth_year, self.planet_id, self.id))
            CONN.commit()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM characters"
        CURSOR.execute(sql)
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM characters WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None

    def delete(self):
        sql = "DELETE FROM characters WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @property
    def planet(self):
        return Planet.find_by_id(self.planet_id)