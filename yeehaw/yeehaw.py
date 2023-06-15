import os
import sys
import time


# File paths for storing character and settings data
character_data_file = "character_data.txt"
settings_data_file = "settings_data.txt"

# Function for character creation
def create_character():
    player_name = input("Enter your name: ")

    if len(set(player_name.lower())) == 1:
        print("Wow, your name is really weird!")

    birth_month = input("Enter your birth month: ")
    first_pet_name = input("Enter the name of your first pet: ")

    # Display the character creation summary
    print("Character Creation Summary:")
    print("Name:", player_name)
    print("Birth Month:", birth_month)
    print("First Pet's Name:", first_pet_name)

    # Save character data to the file
    with open(character_data_file, "w") as file:
        file.write(player_name + "\n")
        file.write(birth_month + "\n")
        file.write(first_pet_name + "\n")

def settings_menu():
    while True:
        print("You think this game has settings?")
        print("You can change the Flerp setting.")
        flerp_level = input("Please enter the level of Flerp (1-10): ")
        spicy_level = input("Enter your spiciness preference: ")

        print("Settings Summary:")
        print("Flerp level:", flerp_level)
        print("Spicy level:", spicy_level)

        user_input = input("Return to Main Menu? (yes/no): ")
        if user_input.lower() == "yes":
            return True  # Return a value indicating the user wants to go back to the main menu
        elif user_input.lower() == "no":
            print("Returning to Settings Menu...")
            continue  # Continue to the next iteration of the loop to prompt the user again
        else:
            print("Invalid choice. Please try again.")


while True:
    print("Menu:")
    print("1. Game")
    print("2. Settings")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Game logic here
        pass
    elif choice == "2":
        print("You selected settings.")
        if settings_menu():
            continue  # Go back to the main menu
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

# Check if the character data file exists and load character data if available
if os.path.exists(character_data_file):
    with open(character_data_file, "r") as file:
        character_data = file.readlines()
    player_name = character_data[0].strip()
    birth_month = character_data[1].strip()
    first_pet_name = character_data[2].strip()
else:
    player_name = ""
    birth_month = ""
    first_pet_name = ""

# Check if the settings data file exists and load settings if available
if os.path.exists(settings_data_file):
    with open(settings_data_file, "r") as file:
        settings_data = file.readlines()
    flerp_level = settings_data[0].strip()
    spicy_level = settings_data[1].strip()
else:
    flerp_level = ""
    spicy_level = ""

while True:
    # Display the menu options
    print("Menu:")
    print("1. Game")
    print("2. Settings")
    print("3. Option 3")
    print("4. Exit")

    # Get user input
    choice = input("Enter your choice: ")

    # Process the user's choice
    if choice == "1":
        print("You selected Game.")
        print("New Game?")
        new_game_choice = input("Enter 'yes' or 'no': ")
        if new_game_choice.lower() == "yes":
            print("Starting a new game...")
            # Call create_character() function
            create_character()
        elif new_game_choice.lower() == "no":
            print("Continuing the game...")
            # Add your code for continuing the game here
        else:
            print("Invalid choice. Please try again.")

    elif choice == "2":
        print("You selected settings.")
        # Call settings_menu() function
        settings_menu()

    elif choice == "3":
        print("You selected Option 3.")
        # Add code for Option 3 here

    elif choice == "4":
        print("Exiting the program...")
        # add code to close the program
        break

    else:
        print("Invalid choice. Please try again.")
