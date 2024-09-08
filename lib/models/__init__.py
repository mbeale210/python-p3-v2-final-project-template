# lib/models/__init__.py

import sqlite3
from .character import Character
from .planet import Planet
from .base import CONN, CURSOR

# CONN = sqlite3.connect('star_wars.db')
# CURSOR = CONN.cursor()