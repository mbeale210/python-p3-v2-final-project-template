# lib/cli.py

from helpers import (
    exit_program,
    display_all_characters,
    add_delete_character,
    display_planet_details,
    move_character
)

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "1":
            characters_menu()
        elif choice == "2":
            add_delete_character()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice")

def main_menu():
    print("\nMain Menu:")
    print("1. Display all characters")
    print("2. Add/Delete character")
    print("3. Exit program")

def characters_menu():
    while True:
        display_all_characters()
        print("\nCharacters Menu:")
        print("1. Planet details")
        print("2. Move a character")
        print("3. Main menu")
        choice = input("> ")
        if choice == "1":
            display_planet_details()
        elif choice == "2":
            move_character()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()