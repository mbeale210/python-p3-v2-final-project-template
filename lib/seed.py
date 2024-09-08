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
        "Mon Calamari", "Ewok", "Sullustan", "Zabrak", "Trandoshan", "Droid", "Mandalorian"
    ]

    print("Creating planets...")
    planet_objects = []
    for planet_name in planets:
        planet = Planet(
            name=planet_name,
            climate=fake.word(),
            terrain=fake.word(),
            population=random.randint(100000, 100000000000)
        )
        planet.save()
        planet_objects.append(planet)
        print(f"Created planet: {planet.name} with ID: {planet.id}")

    print("Creating characters...")
    for _ in range(50):
        planet = random.choice(planet_objects)
        character = Character(
            name=fake.name(),
            species=random.choice(species),
            birth_year=f"{random.choice(['BBY', 'ABY'])} {random.randint(1, 1000)}",
            planet_id=planet.id
        )
        character.save()
        print(f"Created character: {character.name} assigned to planet: {planet.name} (ID: {planet.id})")

    print("Seeding complete!")