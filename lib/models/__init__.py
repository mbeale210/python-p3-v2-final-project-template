import sqlite3
from .characters import Character
from .planet import Planet

CONN = sqlite3.connect('star_wars.db')
CURSOR = CONN.cursor()
