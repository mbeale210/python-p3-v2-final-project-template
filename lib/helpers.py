# lib/helpers.py
from models.characters import Character
from models.planets import Planet


# def helper_1():
#     print("Performing useful function#1.")

def exit_program():
    print("May the Force be with You!")
    exit()

def display_all_characters():
    characters = Character.get_all()
    for character in characters:
        planet = Planet.find_by_id(character.planet_id)
        print(f"{character.name} - Species: {character.species}, Planet: {planet.name}")

def add_delete_character():
    print()

def display_planet_details():
    print()

def move_character():
    print()

