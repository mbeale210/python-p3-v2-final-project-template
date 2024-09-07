import random
from faker import Faker
from models.character import Character
from models.planet import Planet

if __name__ == "__main__":
    print("Resetting tables...")
    Character.drop_table()
    Planet.drop_table()
    Character.create_table()
    Planet.create_table()

    fake = Faker()

    planets = [
        "Tatooine", "Alderaan", "Hoth", "Dagobah", "Bespin", "Endor", "Naboo",
        "Coruscant", "Kamino", "Geonosis", "Utapau", "Mustafar", "Kashyyyk"
    ]

    species = [
        "Human", "Wookiee", "Twi'lek", "Rodian", "Hutt", "Gungan", "Togruta",
        "Mon Calamari", "Ewok", "Sullustan", "Zabrak", "Trandoshan", "Droid"
    ]

    