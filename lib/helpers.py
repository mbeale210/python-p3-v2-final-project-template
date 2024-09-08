from models.character import Character
from models.planet import Planet

def exit_program():
    print("""

                      .::===-:.          ::.
                    .++==+===-:::....:+#@%=.
                  .=***+**=++--::=**%@%@-.
                 .:***###*==+====+*##%%-.
                .:-#%#*#**+*#####**#*:.                May The Force 
            .:=+*#*#%####%%%%##**+*:.                    Be With You
         .=*#%%%%%%%#%#%%%*+#####%*-==-:.
               .::.*%%##%%#***%@%@%#%%**%=.    .:.
                    .=%%%###%#@@@%%###*%*#%+...##%-.
                   .#@*%%@@@@@@@%%%#%#@#+*#*##%%%-:=-.
                   .@@**%%%@@@@%#%%%#%@###%%%%%%%%%%#:.
                  .=@@%%%%%%%%@%#%%%#%@%%%%%#%%%%%*.
                 .:#@@%%%%%%%%%%#%%%%%@%###@@@%%%@*.
                .:*%@@%%%%%%%%%#%@#%%%@%###%@@@@@@+.
            .-%#%@@@@%%%%%%%%%%@#%%%@%%##%@@@@@@=.
          .:--+%@@%%@@@@%**#%%@%%@%@%%@@%###@@@@@@+.
         .==**%%@@%%@@@%%###%%@%@@%@@%@@%%%#%@@@@@#.
        .-=*#%@%@@%%@@@@%%%%%@@@@%%@@%%@#*=*#@@@@@%-.
     .:#%%###@@%@@#%%@@@%%%%%%@@@#%@@%%%#+=-##@@@@%=.
     .-%%%%%%%%%@%#%%@@@%%%%%%%@@%#%@@%%#+=..=#@@@%=.
       .:-+@+%%%@@%#%@@@@@%%%%%%@@%%%@@%%#*+....:--:.
        .-@.-%%@@*#%@@@@@%%%%%%@%%%%@@%%**=:.
        .-@=..:=+*#%@%@@@%%%%%%@%%%#%@%%#*=:.
        .-@%....:*##%@@@@%%%%%%%%#%##@@##*=-.
        .:%@=...:*##%%%@@%%%%%%%%#%##@@#**+-.
         .*@%...-###%%%@@%%%@@%%%#%#*%@#*++=:.
         .:@@...+###%%%@@%%%@@%%%#%#*%@#*+++=.
          .@@=..###%%%%@@%%%@@@%%#%%*%@#*++++-.
          .#@#.:###%%%%@%%%@@@@@%#%%*%@%*++*++:.
          .=@#.+###%%%%@%%%@@@@%##%%*#@%*+=+++-.
           .##.*###%%%%@@%%@@@@%##%%*#@@*+++++=.
           .*#.*###%%%%@@%@@@@@%*#%%*#@@#*+++++:.
           .+%-*####%%%@@%@@@@@%*#%%#*@@#*+++++.
           .-@=######%%@@@@@@@@@*#@%#*@@%*+++++-.
            .%##%%###%@@@@@@@@@%*#@@##@@%*+++++=:.
             .+.=%@@@@@@@@@@@@@%#%@@##@@%#*++++*+=:.
            .-*#*#*##%@@@@@@##%*+=+++@@@@@@%#@@@%%:.
                                    .+%@@@@@#+#@%%-.
    """)
    exit()

def display_all_characters():
    characters = Character.get_all()
    for character in characters:
        planet = character.planet
        planet_name = planet.name if planet else "Unknown"
        print(f"{character.id}. {character.name} - Species: {character.species}, Planet: {planet_name}")

def add_delete_character():
    print("\n1. Add Character")
    print("2. Delete Character")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter hero name: ")
        species = input("Enter hero species: ")
        birth_year = input("Enter hero birth year. please start with BBY or ABY: ")
        planets = Planet.get_all()
        print("Available planets:")
        for planet in planets:
            print(f"{planet.id}. {planet.name}")
        planet_id = int(input("Enter planet ID: "))
        character = Character(name, species, birth_year, planet_id)
        character.save()
        print("Your Hero is ready to travel the galaxy!")
    elif choice == "2":
        characters = Character.get_all()
        for character in characters:
            print(f"{character.id}. {character.name}")
        character_id = int(input("Enter character ID to delete: "))
        character = Character.find_by_id(character_id)
        if character:
            character.delete()
            print("Your Hero has become one with the force!")
        else:
            print("It seems the Hero you are looking for does not exist.")
    else:
        print("Invalid choice. I find your lack of faith disturbing")

def display_planet_details():
    display_all_planets()
    planet_id = int(input("Would you like to learn more? Enter planet ID: "))
    planet = Planet.find_by_id(planet_id)
    if planet:
        print("""
                                                                      ..;===+.
                                                                  .:=iiiiii=+=
                                                               .=i))=;::+)i=+,
                                                            ,=i);)I)))I):=i=;
                                                         .=i==))))ii)))I:i++
                                                       +)+))iiiiiiii))I=i+:'
                                  .,:;;++++++;:,.       )iii+:::;iii))+i='
                               .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                             ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                           ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                          ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                        ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                       ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                      ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                      =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                     +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                     =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                    .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                    :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                    :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                    .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                    =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                  +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
                +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
               =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
             +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
           :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
         .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
        ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
       +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
     .+=:))iiiiiiii)))+ii;
    .+=;))iiiiii)));ii+
   .+=i:)))))))=+ii+
  .;==i+::::=)i=;
  ,+==iiiiii+,
  `+=+++;`
        """)
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
        print("It seems the system you are looking for does not exist.")

def move_character():
    characters = Character.get_all()
    for character in characters:
        planet = character.planet
        planet_name = planet.name if planet else "Unknown"
        print(f"{character.id}. {character.name} - Current planet: {planet_name}")
    character_id = int(input("Enter character ID to move: "))
    character = Character.find_by_id(character_id)
    if character:
        planets = Planet.get_all()
        print("Available planets:")
        for planet in planets:
            print(f"{planet.id}. {planet.name}")
        new_planet_id = int(input("Enter new planet ID: "))
        character.planet_id = new_planet_id
        character.save()
        print("Your Hero has made the jump to light speed!")
    else:
        print("It seems the Hero you are looking for does not exist.")

def display_all_planets():
    planets = Planet.get_all()
    print("\nAll Planets:")
    for planet in planets:
        print(f"{planet.id}. {planet.name}")

