import re

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
            while True:
                # Perform character creation
                print("Character Creation")
                # Add your code for character creation here
                while True:
                    player_name = input("Enter your name: ")
                    if re.match(r'^[a-zA-Z0-9\s]+$', player_name):
                        break
                    else:
                        print("Invalid input. Please enter a name without special characters.")
                # If character creation is complete, break out of the nested loop
                break
        elif new_game_choice.lower() == "no":
            print("Continuing the game...")
            # Add your code for continuing the game here
        else:
            print("Invalid choice. Please try again.")
    elif choice == "2":
        print("You selected settings.")
        # Add code for settings here
        print("You think this game has settings?")
        # Code here to return to the main menu after a delay or if the player enters 'x'
    elif choice == "3":
        print("You selected Option 3.")
        # Add code for Option 3 here
    elif choice == "4":
        print("Exiting the program...")
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")
