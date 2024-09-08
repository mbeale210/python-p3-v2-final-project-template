# lib/helpers.py
from lib.models import Character, Planet

def exit_program():
    print("May the Force be with You!")
    exit()

def display_all_characters():
    characters = Character.get_all()
    if not characters:
        print("No characters found in the galaxy.")
    else:
        print("\n=== Characters in the Galaxy ===")
        for character in characters:
            planet = Planet.find_by_id(character.planet_id)
            print(f"{character.name} - Species: {character.species}, Planet: {planet.name if planet else 'Unknown'}")

def add_character():
    name = input("Enter character name: ")
    species = input("Enter character species: ")
    birth_year = input("Enter character birth year: ")
    display_all_planets()
    planet_id = int(input("Enter planet ID: "))
    
    character = Character(name, species, birth_year, planet_id)
    character.save()
    print(f"{name} has joined the galaxy!")

def delete_character():
    display_all_characters()
    character_id = int(input("Enter character ID to delete: "))
    character = Character.find_by_id(character_id)
    if character:
        character.delete()
        print(f"{character.name} has become one with the Force.")
    else:
        print("Character not found in our records.")

def display_all_planets():
    planets = Planet.get_all()
    if not planets:
        print("No planets found in the galaxy.")
    else:
        print("\n=== Planets in the Galaxy ===")
        for planet in planets:
            print(f"{planet.id}. {planet.name}")

def add_planet():
    name = input("Enter planet name: ")
    climate = input("Enter planet climate: ")
    terrain = input("Enter planet terrain: ")
    population = int(input("Enter planet population: "))
    
    planet = Planet(name, climate, terrain, population)
    planet.save()
    print(f"{name} has been added to the galaxy!")

def delete_planet():
    display_all_planets()
    planet_id = int(input("Enter planet ID to delete: "))
    planet = Planet.find_by_id(planet_id)
    if planet:
        planet.delete()
        print(f"{planet.name} has been destroyed.")
    else:
        print("Planet not found in our records.")

def display_planet_details():
    display_all_planets()
    planet_id = int(input("Enter planet ID for details: "))
    planet = Planet.find_by_id(planet_id)
    if planet:
        print(f"\nPlanet: {planet.name}")
        print(f"Climate: {planet.climate}")
        print(f"Terrain: {planet.terrain}")
        print(f"Population: {planet.population}")
        characters = Character.get_all()
        planet_characters = [c for c in characters if c.planet_id == planet.id]
        print("\nCharacters on this planet:")
        for character in planet_characters:
            print(f"- {character.name} ({character.species})")
    else:
        print("Planet not found in our records.")

def move_character():
    display_all_characters()
    character_id = int(input("Enter character ID to move: "))
    character = Character.find_by_id(character_id)
    if character:
        display_all_planets()
        new_planet_id = int(input("Enter new planet ID: "))
        new_planet = Planet.find_by_id(new_planet_id)
        if new_planet:
            character.planet_id = new_planet_id
            character.save()
            print(f"{character.name} has been moved to {new_planet.name}.")
        else:
            print("Destination planet not found in our records.")
    else:
        print("Character not found in our records.")

def find_character_by_name(name):
    characters = Character.get_all()
    found_characters = [c for c in characters if name.lower() in c.name.lower()]
    if found_characters:
        print("\n=== Found Characters ===")
        for character in found_characters:
            planet = Planet.find_by_id(character.planet_id)
            print(f"{character.name} - Species: {character.species}, Planet: {planet.name if planet else 'Unknown'}")
    else:
        print(f"No characters found with the name '{name}'.")

def find_planet_by_name(name):
    planets = Planet.get_all()
    found_planets = [p for p in planets if name.lower() in p.name.lower()]
    if found_planets:
        print("\n=== Found Planets ===")
        for planet in found_planets:
            print(f"{planet.name} - Climate: {planet.climate}, Terrain: {planet.terrain}")
    else:
        print(f"No planets found with the name '{name}'.")