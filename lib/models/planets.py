from .base import Base, CURSOR, CONN

class Planet(Base):
    table_name = "planets"

    def __init__(self, name, climate, terrain, population, id=None):
        self.id = id
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.population = population