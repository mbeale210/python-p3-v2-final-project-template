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
    print("\n1. Add Character")
    print("2. Delete Character")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your hero's name: ")
        species = input("Enter hero species: ")
        birth_year = input("Enter hero birth year: ")
        planets = Planet.get_all()
        print("Available planets:")
        for planet in planets:
            print(f"{planet.id}. {planet.name}")
        planet_id = int(input("Enter planet ID: "))
        character = Character(name, species, birth_year, planet_id)
        character.save()
        print("Your hero is ready to Adventure!")
    elif choice == "2":
        characters = Character.get_all()
        for character in characters:
            print(f"{character.id}. {character.name}")
        character_id = int(input("Enter character ID to delete: "))
        character = Character.find_by_id(character_id)
        if character:
            character.delete()
            print("Your hero has become one with the Force!")
        else:
            print("Hero is nowhere in the galaxy.")    

def display_planet_details():
    print()

def move_character():
    print()

