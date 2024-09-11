# Star Wars Character Management CLI

This Command Line Interface (CLI) application allows users to manage a database of Star Wars characters and planets. Users can view, add, delete, and move characters between planets.

## Main Features

- Display all characters
- Add/Delete characters
- View planet details
- Move characters between planets

## ERD:
PLANET ||--o{ CHARACTER: “has many”
PLANET {
int id PK
string name
string climate
string terrain
int population
}
CHARACTER {
int id PK
string name
string species
string birth_year
int panet_id FK
{

## File Structure

### lib/cli.py
This is the main entry point of the application. It contains the following key functions:

- `main()`: The main loop of the CLI that presents the user with the main menu.
- `main_menu()`: Displays the main menu options.
- `characters_menu()`: Handles the sub-menu for character-related actions.

### lib/helpers.py
This file contains helper functions that are used throughout the CLI:

- `display_all_characters()`: Prints a list of all characters with their details.
- `add_delete_character()`: Handles adding or deleting a character.
- `display_planet_details()`: Shows detailed information about a specific planet.
- `move_character()`: Allows moving a character from one planet to another.
- `display_all_planets()`: Lists all available planets.

### lib/models/character.py
Defines the `Character` class, which represents a Star Wars character. Key methods include:

- `save()`: Saves or updates a character in the database.
- `get_all()`: Retrieves all characters from the database.
- `find_by_id()`: Finds a character by their ID.
- `delete()`: Removes a character from the database.

### lib/models/planet.py
Defines the `Planet` class, representing a Star Wars planet. Similar to the `Character` class, it includes methods for database operations.

### lib/seed.py
This script populates the database with initial data, creating a set of planets and characters to start with.

## How to Use

1. Run `python lib/seed.py` to populate the database with initial data.
2. Start the CLI by running `python lib/cli.py`.
3. Navigate through the menus to manage characters and planets.

## Dependencies

- Python 3.x
- SQLite3

## Future Improvements

- Add more detailed character attributes (e.g., force-alignment, force sensitivity)
- Implement a search function for characters and planets
- Add a vehicle model that will allow many-to-many relationships

Feel free to contribute to this project by submitting pull requests or reporting issues!

May the Force be with you!

---

ASCII art thanks to:
- https://www.asciiart.eu/movies/star-wars
- https://asciiart.website/index.php?art=movies/star%20wars
- https://emojicombos.com/star-wars-ascii-art



## Console Layout
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── base.py
    │   ├── character.py
    │   └── planet.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py

## The Entire Star Wars Movie in ASCII art

https://www.asciimation.co.nz/