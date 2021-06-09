# Module Six Milestone for IT-140 by Grant Virtue
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
# Added Wine Room to ensure that directions work with new rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom', 'South': 'Wine Room'},
        'Wine Room': {'North': 'Cellar'}
    }

# Initializing player_choice to prevent exit-on-start condition
player_choice = 0

# setting starting location to 'Great Hall' and placing player in starting location. Likely
# this is unnecessary, but adding for clarity and later enhancement.
starting_loc = 'Great Hall'
player_loc = starting_loc

# Instructions here. For this simple program the commands are case sensitive. For live version
# case will be made to not matter.
print('Welcome to my home, friend! Feel free to explore as long as you please')
print('Valid commands are ''North'', ''East'', ''South'', and ''West')
print('Enter ''Exit'' to leave my home\n\n')

# Keep looping while the player is not exiting. Partially made redundant by the exit statement in the ELIF
# Loop below
while player_choice != 'Exit':
    print('Your current location is: {}'.format(player_loc))
    player_choice = input()

# Test to make sure the player is entering a valid direction
    if player_choice == 'North' or player_choice == 'South' or player_choice == 'East' or player_choice == 'West':
        if player_choice in rooms[player_loc]:
            player_loc = rooms[player_loc][player_choice]
        else:
            print('There is no room in that direction.')
    # If the player chooses Exit then let them know that the game is over by printing something.
    elif player_choice == 'Exit':
        print('Thank you for playing!')
        exit()
    # Throw out all other commands and bring them back to the beginning of the while loop.
    else:
        print('Invalid choice, friend!')
