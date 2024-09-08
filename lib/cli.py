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
            print("Invalid choice. I find your lack of faith disturbing.")

def main_menu():
    print("\nMain Menu:")
    print("1. Let's find some Heroes")
    print("2. Add/Delete Hero")
    print("3. Exit program")

def characters_menu():
    while True:
        display_all_characters()
        print("\nCharacters Menu:")
        print("1. Planet details")
        print("2. Move a hero")
        print("3. Main menu")
        choice = input("> ")
        if choice == "1":
            display_planet_details()
            break
        elif choice == "2":
            move_character()
            break
        elif choice == "3":
            break
        else:
            print("Invalid choice. I find your lack of faith disturbing.")

if __name__ == "__main__":
    main()