import random

# Define constants
FIELD_SIZE = 40
HUMAN_PLAYER = 1
COMPUTER_ENEMY = 2
RESOURCE_LABEL = "Resources: "
HUMAN_RESOURCES = 1000
COMPUTER_RESOURCES = 1000

# Define game objects
EMPTY = 0
HUMAN_BASE = 1
HUMAN_STRUCTURE = 2
HUMAN_UNIT = 3
COMPUTER_BASE = 4
COMPUTER_STRUCTURE = 5
COMPUTER_UNIT = 6
RESOURCES_PER_STRUCTURE = 5

# Initialize game field
field = [[EMPTY for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]
field[0][0] = HUMAN_BASE
field[FIELD_SIZE-1][FIELD_SIZE-1] = COMPUTER_BASE

# Initialize resources
human_resources = HUMAN_RESOURCES
computer_resources = COMPUTER_RESOURCES


# Define helper functions
def count_structures(player):
    count = 0
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if field[i][j] == player + 1:
                count += 1
    return count

# Define helper functions
def print_field():
    for i in range(FIELD_SIZE):
        row = ""
        for j in range(FIELD_SIZE):
            if field[i][j] == EMPTY:
                row += "   "
            elif field[i][j] == HUMAN_BASE:
                row += " H "
            elif field[i][j] == HUMAN_STRUCTURE:
                row += " h "
            elif field[i][j] == HUMAN_UNIT:
                row += " u "
            elif field[i][j] == COMPUTER_BASE:
                row += " C "
            elif field[i][j] == COMPUTER_STRUCTURE:
                row += " c "
            elif field[i][j] == COMPUTER_UNIT:
                row += " e "
        print(row)
        
def print_resources():
    print(RESOURCE_LABEL + "Human: " + str(human_resources) + "   Computer: " + str(computer_resources))

def collect_resources(resource_truck):
    if resource_truck == 1:
        human_resources += 1
    elif resource_truck == 2:
        computer_resources += 1

def get_random_empty_location():
    while True:
        i = random.randint(0, FIELD_SIZE-1)
        j = random.randint(0, FIELD_SIZE-1)
        if field[i][j] == EMPTY:
            return i, j

"""
def get_attack_unit(field, position(i,j), player):
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if (field[i][j] == HUMAN_UNIT or field[i][j] == COMPUTER_UNIT) and abs(i - position[0]) <= 1 and abs(j - position[1]) <= 1 and (i, j) != position and field[i][j] != player:
                return (i, j)
    return None
"""

# Main game loop
while True:

    # Collect resources for human player
    human_resources += count_structures(HUMAN_PLAYER) * RESOURCES_PER_STRUCTURE

    # Print game field and resources
    print_field()
    print_resources()
    
    #get_attack_unit(field(i,j), position(i,j), player(HUMAN_PLAYER,COMPUTER_ENEMY))
    #print(get_attack_unit())


    # Human player's turn (same code as before)

    

    # Computer's turn (same code as before)

    # Check for game over (same code as before)



    # Get user input
    while True:
        print("What do you want to do?")
        print("1. Build structure")
        print("2. Train unit")
        choice = input("Enter choice: ")
        if choice == "1":
            print("Which structure do you want to build?")
            print("1. Human structure (cost: 10 resources)")
            print("2. Computer structure (cost: 10 resources)")
            structure_choice = input("Enter choice: ")
            if structure_choice == "1":
                if human_resources >= 10:
                    i, j = get_random_empty_location()
                    field[i][j] = HUMAN_STRUCTURE
                    human_resources -= 10
                    break
                else:
                    print("Not enough resources!")
            elif structure_choice == "2":
                if human_resources >= 10:
                    i, j = get_random_empty_location()
                    field[i][j] = COMPUTER_STRUCTURE
                    human_resources -= 10
                    break
                else:
                    print("Not enough resources!")
            else:
                print("Invalid choice!")
        elif choice == "2":
            if human_resources >= 5:
                i, j = get_random_empty_location()
                field[i][j] = HUMAN_UNIT
                human_resources -= 5
                break
            else:
                print("Not enough resources!")
        else:
            print("Invalid choice!")
    
    # Collect resources for computer player
    computer_resources += count_structures(COMPUTER_ENEMY) * RESOURCES_PER_STRUCTURE        
    
    # Computer's turn
    if computer_resources >= 10:
        i, j = get_random_empty_location()
        field[i][j] = COMPUTER_STRUCTURE
        computer_resources -= 10
    if computer_resources >= 5:
        i, j = get_random_empty_location()
        field[i][j] = COMPUTER_UNIT
        computer_resources -= 5
    
    # Check for game over
    if human_resources == 0 and computer_resources == 0:
        print("Game over! It's a tie!")
        break
    elif human_resources == 0:
        print("Game over! You lost!")
        break
    elif computer_resources == 0:
        print("Game over! You won!")
        break

"""

To give units the ability to attack and add a delay to structure construction, we can make the following changes:

1.Add a constant for the number of turns required to construct a structure.
2.Add a constant for unit attack range.
3.Modify the field representation to include structure construction progress and unit health.
4.Add helper functions to count down construction progress and perform unit attacks.
5.Update the main game loop to include structure construction progress and unit attacks.


# Define constants
TURNS_TO_BUILD_STRUCTURE = 3
UNIT_ATTACK_RANGE = 1

# Modify the field representation
field = [[(EMPTY, 0, 0) for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]
field[0][0] = (HUMAN_BASE, 0, 0)
field[FIELD_SIZE-1][FIELD_SIZE-1] = (COMPUTER_BASE, 0, 0)

# Update the print_field function
def print_field():
    for i in range(FIELD_SIZE):
        row = ""
        for j in range(FIELD_SIZE):
            tile, construction_progress, unit_health = field[i][j]
            if tile == EMPTY:
                row += "   "
            elif tile == HUMAN_BASE:
                row += " H "
            elif tile == HUMAN_STRUCTURE:
                row += " h "
            elif tile == HUMAN_UNIT:
                row += " u "
            elif tile == COMPUTER_BASE:
                row += " C "
            elif tile == COMPUTER_STRUCTURE:
                row += " c "
            elif tile == COMPUTER_UNIT:
               

                
"""