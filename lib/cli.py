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
        print("""
                                            
          ________________   ___      ______
         /                | /   \    |   _  \.
        |   (-----|  |----`/  ^  \   |  |_)  |
         \   \    |  |    /  /_\  \  |      /
    .-----)   |   |  |   /  _____  \ |  |\  \-------.
    |________/    |__|  /__/     \__\| _| `.________|
     ____    __    ____  ___     .______    ________.
     \   \  /  \  /   / /   \    |   _  \  /        |
      \   \/    \/   / /  ^  \   |  |_)  ||   (-----`
       \            / /  /_\  \  |      /  \   \.
        \    /\    / /  _____  \ |  |\  \---)   |
         \__/  \__/ /__/     \__\|__| `._______/

------------------------------------------------
         _    _  _____ ____    ____  
        | |  | |/ ____|  _ \  / __ \  
        | |__| | |____| |_)  | |  | | 
        |  __  |  ____|  _ < | |  | | 
        | |  | | |____| | \ \| |__| |        
        |_|  |_|\_____|_|  \ \_____/  
     __  __  ______      ________ ____  
    |  \/  |/ __ \ \    / /  ____|  _ \ 
    | \  / | |  | \ \  / /| |__  | |_) |
    | |\/| | |  | |\ \/ / |  __| |  _ < 
    | |  | | |__| | \  /  | |____| | \ \-------.
    |_|  |_|\____/   \/   |______|_|  \________|.


        """)
        main_menu()
        choice = input("> ")
        if choice == "1":
            characters_menu()
        elif choice == "2":
            add_delete_character()
        elif choice == "3":
            exit_program()
        else:
            print("""
                       .-.
                      |_:_|
                     /(_Y_)\.
.                   ( \/M\/ )      I find your lack of faith disturbing.
 '.               _.'-/'-'\-'._
   ':           _/.--'[[[[]'--.\_
     ':        /_'  : |::"| :  '.\.
       ':     //   ./ |oUU| \.'  :\.
         ':  _:'..' \_|___|_/ :   :|
           ':.  .'  |_[___]_|  :.':\.
            [::\ |  :  | |  :   ; : \.
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :   \.
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
          |     : : :_/_|  /'._\  '--|_\.
          /___.-/_|-'   \  \.
                         '-'
                  
                  Invalid choice. 

                  Art by Shanaka Dias
                  """)

def main_menu():
    print("\nMain Menu:")
    print("1. Let's find some Heroes")
    print("2. Add/Delete Hero")
    print("3. Exit program")

def characters_menu():
    while True:
        print("""
⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣧⠷⠆⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣐⣢⣤⢖⠒⠪⣭⣶⣿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣌⠀⢀⣿⠁⢹⣿⡇⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⡿⠿⢖⡪⠅⢂⠀⠀⠀⠀⠀⠀Beep Beep Boop
⠀⠀⢀⣔⣒⣒⣂⣈⣉⣄⠀⠺⣿⠿⣦⡀⠀⠀⠀    Translation:
⠀⡴⠛⣉⣀⡈⠙⠻⣿⣿⣷⣦⣄⠀⠛⠻⠦⠀⠀         How can I be of assistance?
⡸⠁⢾⣿⣿⣁⣤⡀⠹⣿⣿⣿⣿⣿⣷⣶⣶⣤⠀
⡇⣷⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⡿⠿⣿⡀
⡇⢿⣿⣿⣿⣟⠛⠃⠀⣿⣿⣿⡿⠋⠁⣀⣀⡀⠃
⢻⡌⠀⠿⠿⠿⠃⠀⣼⣿⣿⠟⠀⣠⣄⣿⣿⡣⠀
⠈⢿⣶⣤⣤⣤⣴⣾⣿⣿⡏⠀⣼⣿⣿⣿⡿⠁⠀
⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⠀⠀⣩⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠿⠿⠿⠇⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
        display_all_characters()
        print("\nHeroes Menu:")
        print("1. Planet details")
        print("2. Move a hero")
        print("3. Main menu")
        choice = input("> ")
        if choice == "1":
            display_planet_details()
        elif choice == "2":
            move_character()
            break
        elif choice == "3":
            break
        else:
            print("""
                       .-.
                      |_:_|
                     /(_Y_)\.
.                   ( \/M\/ )      I find your lack of faith disturbing.
 '.               _.'-/'-'\-'._
   ':           _/.--'[[[[]'--.\_
     ':        /_'  : |::"| :  '.\.
       ':     //   ./ |oUU| \.'  :\.
         ':  _:'..' \_|___|_/ :   :|
           ':.  .'  |_[___]_|  :.':\.
            [::\ |  :  | |  :   ; : \.
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :   \.
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
          |     : : :_/_|  /'._\  '--|_\.
          /___.-/_|-'   \  \.
                         '-'
                  
                  Invalid choice. 

                  Art by Shanaka Dias
                  """)


if __name__ == "__main__":
    main()