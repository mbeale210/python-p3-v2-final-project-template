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
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            display_all_characters()
        elif choice == "2":
            add_delete_character()
        elif choice == "3":
            display_planet_details()
        elif choice == "4":
            move_character()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Display all characters")
    print("2. Add/Delete character")
    print("3. Display planet details")
    print("4. Move character to a different planet")

if __name__ == "__main__":
    main()