# lib/cli.py

from helpers import (
    exit_program,
    display_all_characters,
    add_character,
    delete_character,
    display_all_planets,
    add_planet,
    delete_planet,
    display_planet_details,
    move_character,
    find_character_by_name,
    find_planet_by_name
)

def main_menu():
    print("\n=== Star Wars Galaxy Explorer ===")
    print("1. Character Management")
    print("2. Planet Management")
    print("3. Exit")

def character_menu():
    print("\n=== Character Management ===")
    print("1. Display all characters")
    print("2. Add a character")
    print("3. Delete a character")
    print("4. Move a character to a different planet")
    print("5. Find a character by name")
    print("6. Return to main menu")

def planet_menu():
    print("\n=== Planet Management ===")
    print("1. Display all planets")
    print("2. Add a planet")
    print("3. Delete a planet")
    print("4. Display planet details")
    print("5. Find a planet by name")
    print("6. Return to main menu")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            handle_character_menu()
        elif choice == "2":
            handle_planet_menu()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def handle_character_menu():
    while True:
        character_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            display_all_characters()
        elif choice == "2":
            add_character()
        elif choice == "3":
            delete_character()
        elif choice == "4":
            move_character()
        elif choice == "5":
            name = input("Enter character name to search: ")
            find_character_by_name(name)
        elif choice == "6":
            return
        else:
            print("Invalid choice. Please try again.")

def handle_planet_menu():
    while True:
        planet_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            display_all_planets()
        elif choice == "2":
            add_planet()
        elif choice == "3":
            delete_planet()
        elif choice == "4":
            display_planet_details()
        elif choice == "5":
            name = input("Enter planet name to search: ")
            find_planet_by_name(name)
        elif choice == "6":
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()