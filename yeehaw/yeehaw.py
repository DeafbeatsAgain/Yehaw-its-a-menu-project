import os
import time

# File path for storing character data
data_file = "character_data.txt"

# Check if the data file exists
if os.path.exists(data_file):
    # Read character data from the file
    with open(data_file, "r") as file:
        character_data = file.readlines()
    # Extract the saved values
    player_name = character_data[0].strip()
    birth_month = character_data[1].strip()
    first_pet_name = character_data[2].strip()
else:
    player_name = ""
    birth_month = ""
    first_pet_name = ""

while True:
    # Display the menu options
    print("Menu:")
    print("1. Game")  # new game or continue
    print("2. Settings")
    print("3. Option 3")  # I don't actually want to code anything here except a dead end.
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
            while True:
                # Perform character creation
                print("Character Creation")
                if not player_name:
                    player_name = input("Enter your name: ")
                
                if len(set(player_name.lower())) == 1:
                    print("Wow, your name is really weird!")
                
                if not birth_month:
                    birth_month = input("Enter your birth month: ")

                if not first_pet_name:
                    first_pet_name = input("Enter the name of your first pet: ")

                # Display the character creation summary
                print("Character Creation Summary:")
                print("Name:", player_name)
                print("Birth Month:", birth_month)
                print("First Pet's Name:", first_pet_name)
                
                # Save character data to the file
                with open(data_file, "w") as file:
                    file.write(player_name + "\n")
                    file.write(birth_month + "\n")
                    file.write(first_pet_name + "\n")
                
                # If character creation is complete, break out of the nested loop
                break

        elif new_game_choice.lower() == "no":
            print("Continuing the game...")
            # Add your code for continuing the game here

        else:
            print("Invalid choice. Please try again.")  # returns user to name entry

    elif choice == "2":
        print("You selected settings.")
        # Add code for settings here
        print("You think this game has settings?")
        print("You can change the lerp setting.")
        print("Please enter the level of Flerp (1-10): ")

        # Add a time delay of 2 seconds
        time.sleep(2)

    elif choice == "3":
        print("You selected Option 3.")
        # Add code for Option 3 here

    elif choice == "4":
        print("Exiting the program...")
        break  # Exit the loop

    else:
        print("Invalid choice. Please try again.")
