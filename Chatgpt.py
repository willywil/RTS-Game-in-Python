import random

# Define constants
FIELD_SIZE = 20
HUMAN_PLAYER = 1
COMPUTER_ENEMY = 2
RESOURCE_LABEL = "Resources: "
HUMAN_RESOURCES = 100
COMPUTER_RESOURCES = 100

# Define game objects
EMPTY = 0
HUMAN_BASE = 1
HUMAN_STRUCTURE = 2
HUMAN_UNIT = 3
COMPUTER_BASE = 4
COMPUTER_STRUCTURE = 5
COMPUTER_UNIT = 6

# Initialize game field
field = [[EMPTY for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]
field[0][0] = HUMAN_BASE
field[FIELD_SIZE-1][FIELD_SIZE-1] = COMPUTER_BASE

# Initialize resources
human_resources = HUMAN_RESOURCES
computer_resources = COMPUTER_RESOURCES

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
        
def get_random_empty_location():
    while True:
        i = random.randint(0, FIELD_SIZE-1)
        j = random.randint(0, FIELD_SIZE-1)
        if field[i][j] == EMPTY:
            return i, j

# Main game loop
while True:
    # Print game field and resources
    print_field()
    print_resources()
    
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